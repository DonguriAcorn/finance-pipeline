WITH source AS (
    SELECT * FROM {{ source('finance_raw', 'vt_raw') }}
),

deduped AS (
    SELECT *
    FROM source
    QUALIFY ROW_NUMBER() OVER (PARTITION BY Date ORDER BY Date) = 1
),

renamed AS (
    SELECT
        Date AS date,
        Open AS open,
        High AS high,
        Low AS low,
        Close AS close,
        Volume AS volume
    FROM deduped
    WHERE Date IS NOT NULL
)

SELECT * FROM renamed