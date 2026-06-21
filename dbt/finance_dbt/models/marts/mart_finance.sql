WITH sp500 AS (
    SELECT * FROM {{ ref('stg_sp500') }}
),

vt AS (
    SELECT * FROM {{ ref('stg_vt') }}
),

usdjpy AS (
    SELECT * FROM {{ ref('stg_usdjpy') }}
)

SELECT
    sp500.date,
    sp500.close AS sp500_close,
    sp500.volume AS sp500_volume,
    vt.close AS vt_close,
    vt.volume AS vt_volume,
    usdjpy.close AS usdjpy_close
FROM sp500
LEFT JOIN vt ON sp500.date = vt.date
LEFT JOIN usdjpy ON sp500.date = usdjpy.date