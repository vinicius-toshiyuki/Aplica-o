create or replace view NOT_JUDGED as (
		select
			s.cod subcod,
			arquivo,
			cast(aluno_matr as integer) alumat,
			problema_cod procod,
			lista_cod liscod,
			modulo_cod modcod,
			disc_cod discod,
			lp.cod lincod
		from
			submissao s join LING_PROGR lp on LING_PROGR_COD = lp.cod
		WHERE
			veredito='not judged'
);

create or replace view test as (
		select
			e.cod codigo,
			e.problema_cod procod,
			e.lista_cod liscod,
			e.modulo_cod modcod,
			e.disc_cod discod,
			e.arquivo ent,
			s.arquivo sai
		from entrada e join saida s on e.cod = s.cod
);

-- select
-- 	s.subcod tentativa,
-- 	t.codigo casos_de_teste,
-- 	alumat quem_enviou,
-- 	s.procod,
-- 	s.liscod,
-- 	s.modcod,
-- 	s.discod
-- from
-- 	not_judged s
-- 	join
-- 	test t
-- 	on
-- 		s.procod = t.procod and
-- 		s.liscod = t.liscod and
-- 		s.modcod = t.modcod and
-- 		s.discod = t.discod
-- 	;

create or replace function corrige(in bytea, in bytea, in bytea, in integer)
	returns text as $julgamento$
	DECLARE
		diff bytea;
		textdiff text;
		lo_id_tmp OID;
	BEGIN

		lo_id_tmp := lo_from_bytea(0, $1);
		perform lo_export(lo_id_tmp, '/tmp/entrada'); -- ||$4);
		perform lo_unlink(lo_id_tmp);
		
		lo_id_tmp := lo_from_bytea(0, $2);
		perform lo_export(lo_id_tmp, '/tmp/saida'); -- ||$4);
		perform lo_unlink(lo_id_tmp);

		lo_id_tmp := lo_from_bytea(0, $3);
		perform lo_export(lo_id_tmp, '/tmp/submissao'); -- ||$4);
		perform lo_unlink(lo_id_tmp);

		copy (select 0) to program '/bin/cat /tmp/entrada | /usr/bin/python3 /tmp/submissao > /tmp/resultado';
		-- copy texto from program '/usr/bin/diff /tmp/saida /tmp/resultado > /tmp/diferenca || echo passssssa';
		copy (select 0) to  program '/usr/bin/diff /tmp/saida /tmp/resultado && echo -n correct > /tmp/diferenca || echo -n wrong > /tmp/diferenca';

		select lo_import('/tmp/diferenca') into lo_id_tmp;
		select lo_get(lo_id_tmp) into diff;
		perform lo_unlink(lo_id_tmp);
		select encode(diff, 'escape') into textdiff;

		update SUBMISSAO set VEREDITO = textdiff where cod = $4;

		return textdiff;
	end;
	$julgamento$ language plpgsql;

create or replace function corrige_submissao()
	returns trigger as $$
	BEGIN
		perform
			corrige(t.ent, t.sai, s.arquivo, s.subcod)
		from
			not_judged s
			join
			test t
			on
				s.procod = t.procod and
				s.liscod = t.liscod and
				s.modcod = t.modcod and
				s.discod = t.discod
		;
		return NEW;
	end;
	$$ language plpgsql;

create trigger corrige_submissao_trigger
	after insert on submissao
	execute procedure corrige_submissao();
-- select
-- 	corrige(t.ent, t.sai, s.arquivo, s.subcod) veredito,
-- 	s.subcod tentativa,
-- 	t.codigo casos_de_teste
-- from
-- 	not_judged s
-- 	join
-- 	test t
-- 	on
-- 		s.procod = t.procod and
-- 		s.liscod = t.liscod and
-- 		s.modcod = t.modcod and
-- 		s.discod = t.discod
-- ;

