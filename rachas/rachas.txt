##Codigo utilizado en rachas 
CREATE TABLE historia (
    identificacion TEXT,
    corte_mes DATE,
    saldo NUMERIC
);

CREATE TABLE retiros (
    identificacion TEXT,
    fecha_retiro DATE
);

SELECT COUNT(*) FROM historia;
SELECT COUNT(*) FROM retiros;

SELECT * FROM historia LIMIT 5;
SELECT * FROM retiros LIMIT 5;


--Validaciones 
-- Nulos
SELECT * FROM historia WHERE identificacion IS NULL OR corte_mes IS NULL;

-- Fechas diferentes
SELECT DISTINCT corte_mes FROM historia ORDER BY corte_mes;

-- Duplicados
SELECT identificacion, corte_mes, COUNT(*)
FROM historia
GROUP BY identificacion, corte_mes
HAVING COUNT(*) > 1;

-- Nos quedamos con los valores mas recientes, evitando los duplicados
WITH params AS (
    SELECT 
        DATE '2024-12-31' AS fecha_base,
        3 AS n
),

historia_dedup AS (
    SELECT identificacion, corte_mes, saldo
    FROM (
        SELECT *,
            ROW_NUMBER() OVER (
                PARTITION BY identificacion, corte_mes
                ORDER BY saldo DESC
            ) AS rn
        FROM historia
    ) t
    WHERE rn = 1
),
--clasificamos
niveles AS (
    SELECT *,
        CASE 
            WHEN saldo >= 0 AND saldo < 300000 THEN 'N0'
            WHEN saldo < 1000000 THEN 'N1'
            WHEN saldo < 3000000 THEN 'N2'
            WHEN saldo < 5000000 THEN 'N3'
            ELSE 'N4'
        END AS nivel
    FROM historia_dedup
),

--Agrupamos en gaps and islands
grupos AS (
    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY identificacion ORDER BY corte_mes)
        -
        ROW_NUMBER() OVER (PARTITION BY identificacion, nivel ORDER BY corte_mes)
        AS grupo
    FROM niveles
),

--rachas por fecha 
rachas AS (
    SELECT
        identificacion,
        nivel,
        MIN(corte_mes) AS fecha_inicio,
        MAX(corte_mes) AS fecha_fin,
        COUNT(*) AS racha
    FROM grupos
    GROUP BY identificacion, nivel, grupo
),

--Se aplican reglas de negocio para las rachas ya parametrizadas
rachas_filtradas AS (
    SELECT r.*
    FROM rachas r
    JOIN params p ON 1=1
    WHERE r.racha >= p.n
      AND r.fecha_fin <= p.fecha_base
),

--Ordenamos para dar un ranking
ranking AS (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY identificacion
            ORDER BY racha DESC, fecha_fin DESC
        ) AS rn
    FROM rachas_filtradas
)

--Traemos la mejor racha por cliente
SELECT 
    identificacion,
    nivel,
    racha,
    fecha_fin
FROM ranking
WHERE rn = 1;

