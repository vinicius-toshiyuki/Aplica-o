select
	a.matricula,
	vereditos,
	errados
from
	(select
	 	matricula,
		count(veredito) vereditos
	from
		aluno
		join
		submissao
		on
			matricula = aluno_matr
	group by matricula) a
	join
	(select
	 	matricula,
		count(veredito) errados
	from
		aluno
		join
		submissao
		on
			matricula = aluno_matr and
			veredito = 'wrong'
	group by matricula) b
	on
		a.matricula = b.matricula
;

(select veredito, count(veredito) from submissao join lista on lista_cod = lista.cod and prova = 'S' group by veredito);

CREATE or REPLACE FUNCTION total_provas()
	RETURNS integer as $total_provas$
	DECLARE
		total integer;
	begin
		select count(*) into total from lista join submissao on lista_cod = lista.cod and prova = 'S';
		return total;
	end;
	$total_provas$ LANGUAGE plpgsql;

CREATE or REPLACE FUNCTION total_provas(varchar)
	RETURNS integer as $total_provas$
	DECLARE
		total integer;
	begin
		if $1 = 'wrong' or $1 = 'correct' or $1 = 'not judged'
		then
			select
				count(*) into total
			from
				lista
				join
				submissao
				on
					lista_cod = lista.cod
					and
					prova = 'S'
					and
					veredito = $1
			;
		else
			select
				count(*) into total
			from
				(lista
				 join
				 submissao
				 on
				 	lista_cod = lista.cod
					and
					prova = 'S'
				) sl
				join
				aluno
					on
						matricula = aluno_matr
			where email = $1
			;
		end if;
		return total;
	end;
	$total_provas$ LANGUAGE plpgsql;

-- TODO: mudara para matrícula
CREATE or REPLACE FUNCTION total_provas(varchar, varchar)
	RETURNS integer as $total_provas$
	DECLARE
		total integer;
		emailaluno alias for $1;
		resultado alias for $2;
	begin
		select
				count(*) into total
			from
				(lista
				 join
				 submissao
				 on
				 	lista_cod = lista.cod
					and
					prova = 'S'
					and
					veredito = resultado
				) sl
				join
				aluno
					on
						matricula = aluno_matr
			where email = emailaluno
			;
		return total;
	end;
	$total_provas$ LANGUAGE plpgsql;

CREATE or REPLACE FUNCTION total_provas(integer, integer, integer)
	RETURNS integer as $total_provas$
	DECLARE
		total integer;
		cod_disciplina alias for $1;
		cod_modulo alias for $2;
		cod_lista alias for $3;
	begin
		select
				count(*) into total
			from
				lista l
				join
				problema p
				on
					l.cod = p.lista_cod and
					l.modulo_cod = p.modulo_cod and
					l.disc_cod = p.disc_cod
			where
				l.disc_cod = cod_disciplina and
				l.modulo_cod = cod_modulo and
				l.cod = cod_lista and
				prova = 'S'
			;
		return total;
	end;
	$total_provas$ LANGUAGE plpgsql;

CREATE or REPLACE FUNCTION total_provas(integer, integer, integer, varchar)
	RETURNS integer as $total_provas$
	DECLARE
		total integer;
		cod_disciplina alias for $1;
		cod_modulo alias for $2;
		cod_lista alias for $3;
		emailaluno alias for $4;
		matr integer;
	begin
		select matricula into matr from aluno where email = emailaluno;
				count(*) into total
			from
				(
				select
					l.cod lista_cod,
					l.modulo_cod modulo_cod,
					l.disc_cod disc_cod,
					prova,
					veredito,
					aluno_matr
				from
					lista l
					join
					submissao s
					on
						l.cod = s.lista_cod and
						l.modulo_cod = s.modulo_cod and
						l.disc_cod = s.disc_cod and
						l.disc_cod = cod_disciplina and
						l.modulo_cod = cod_modulo and
						l.cod = cod_lista
				) ls
				join
				problema p
				on
					p.lista_cod = ls.lista_cod and
					p.modulo_cod = ls.modulo_cod and
					p.disc_cod = ls.disc_cod and
			where
				prova = 'S' and
				aluno_matr = matr and
				veredito = 'correct'
			;
		return total;
	end;
	$total_provas$ LANGUAGE plpgsql;


CREATE or REPLACE FUNCTION nota(varchar)
	RETURNS real as $nota$
	DECLARE
		emailaluno alias for $1;
		nota real;
		tprovas integer;
		acertos integer;
	begin
		perform * from (submissao join aluno on aluno_matr = matricula) sub_do_aluno where veredito = 'correct';


		select total_provas() into tprovas;
		select total_provas(emailaluno, 'correct') into acertos;
		nota := cast(tprovas as real) - cast(acertos as real);
		return nota;
	end;
	$nota$ LANGUAGE plpgsql;

select total_provas() total_provas;
select total_provas('wrong') wrong;
select total_provas('correct') correct;
select total_provas('vtmsugimoto@gmail.com'), 'vtmsugimoto@gmail.com' email;
select total_provas('vtmsugimoto@gmail.com', 'wrong') wrong, 'vtmsugimoto@gmail.com' email;
select total_provas('vtmsugimoto@gmail.com', 'correct') correct, 'vtmsugimoto@gmail.com' email;

select nota('vtmsugimoto@gmail.com');

CREATE or REPLACE FUNCTION nota(varchar)
	RETURNS real as $nota$
		DECLARE
			emailaluno alias for $1;
			codigo_disciplina integer;
			qt_modulos integer;
			qt_listas integer;
			i integer;
			j integer;
			qt_provas integer;
			qt_acertos integer;
			ehprova varchar;
		begin
			select 0,0,0,0 into i,j,qt_provas,qt_acertos;
			select disc_cod into codigo_disciplina from aluno where email = emailaluno;
			select count(*) into qt_modulos from modulo where disc_cod = codigo_disciplina;
			raise notice 'codigo da disciplina é %', codigo_disciplina;
			raise notice 'qt modulos é %', qt_modulos;
			loop
				exit when i = qt_modulos;
				select count(*) into qt_listas from lista where modulo_cod = i + 1 and disc_cod = codigo_disciplina;
				raise notice 'qt_listas é %', qt_listas;
				loop
					exit when j = qt_listas;
					
					select prova into ehprova from lista where cod = j + 1 and modulo_cod = i + 1 and disc_cod = codigo_disciplina;
					raise notice 'ehprova é %', ehprova;
					if ehprova = 'S'
					then
						select total_provas(codigo_disciplina, i + 1, j + 1) + qt_provas into qt_provas;
						raise notice 'qt_provas é %', qt_provas;
						select total_provas(codigo_disciplina, i + 1, j + 1, emailaluno) + qt_acertos into qt_acertos;
						raise notice 'qt_acertos é %', qt_acertos;
					end if;

					select j + 1 into j;
				end loop;
				select i + 1 into i;
			end loop;
			if qt_provas = 0
			then
				return 0;
			else
				return cast(qt_acertos as real) / cast(qt_provas as real);
			end if;
		end;
		$nota$ LANGUAGE plpgsql;
