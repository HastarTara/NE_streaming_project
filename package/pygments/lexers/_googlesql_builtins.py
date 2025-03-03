"""
    pygments.lexers._googlesql_builtins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Autogenerated data files for the GoogleSQL lexer.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

constants = [
    'FALSE',
    'NULL',
    'TRUE',
    'UNKNOWN',
]

# Everything below this line is auto-generated from the GoogleSQL source code.
# ----------------------------------------------------------------------------

functionnames = [
    'ABS',
    'ACOS',
    'ACOSH',
    'AEAD.DECRYPT_BYTES',
    'AEAD.DECRYPT_STRING',
    'AEAD.ENCRYPT',
    'AEAD.ENVELOPE_DECRYPT_BYTES',
    'AEAD.ENVELOPE_DECRYPT_STRING',
    'AEAD.ENVELOPE_ENCRYPT',
    'ALL_DIFFERENT',
    'ANON_AVG',
    'ANON_COUNT',
    'ANON_COUNT',
    'ANON_PERCENTILE_CONT',
    'ANON_QUANTILES',
    'ANON_STDDEV_POP',
    'ANON_SUM',
    'ANON_VAR_POP',
    'ANY_VALUE',
    'APPROX_COSINE_DISTANCE',
    'APPROX_COUNT_DISTINCT',
    'APPROX_DOT_PRODUCT',
    'APPROX_EUCLIDEAN_DISTANCE',
    'APPROX_QUANTILES',
    'APPROX_TOP_COUNT',
    'APPROX_TOP_SUM',
    'ARRAY[KEY()]',
    'ARRAY[SAFE_KEY()]',
    'ARRAY_AGG',
    'ARRAY_AVG',
    'ARRAY_CONCAT',
    'ARRAY_CONCAT_AGG',
    'ARRAY_FILTER',
    'ARRAY_FIND',
    'ARRAY_FIND_ALL',
    'ARRAY_FIRST',
    'ARRAY_FIRST_N',
    'ARRAY_INCLUDES',
    'ARRAY_INCLUDES_ALL',
    'ARRAY_INCLUDES_ANY',
    'ARRAY_IS_DISTINCT',
    'ARRAY_LAST',
    'ARRAY_LAST_N',
    'ARRAY_LENGTH',
    'ARRAY_MAX',
    'ARRAY_MIN',
    'ARRAY_OFFSET',
    'ARRAY_OFFSETS',
    'ARRAY_REMOVE_FIRST_N',
    'ARRAY_REMOVE_LAST_N',
    'ARRAY_REVERSE',
    'ARRAY_SLICE',
    'ARRAY_SUM',
    'ARRAY_TO_STRING',
    'ARRAY_TRANSFORM',
    'ARRAY_ZIP',
    'ASCII',
    'ASIN',
    'ASINH',
    'ATAN',
    'ATAN2',
    'ATANH',
    'AVG',
    'BIT_AND',
    'BIT_COUNT',
    'BIT_OR',
    'BIT_XOR',
    'BOOL',
    'BOOL_ARRAY',
    'BYTE_LENGTH',
    'CASE',
    'CAST',
    'CBRT',
    'CEIL',
    'CEILING',
    'CHARACTER_LENGTH',
    'CHAR_LENGTH',
    'CHR',
    'COALESCE',
    'CODE_POINTS_TO_BYTES',
    'CODE_POINTS_TO_STRING',
    'COLLATE',
    'CONCAT',
    'CORR',
    'COS',
    'COSH',
    'COSINE_DISTANCE',
    'COT',
    'COTH',
    'COUNT',
    'COUNT(*)',
    'COUNTIF',
    'COVAR_POP',
    'COVAR_SAMP',
    'CSC',
    'CSCH',
    'CUME_DIST',
    'CURRENT_DATE',
    'CURRENT_DATETIME',
    'CURRENT_TIME',
    'CURRENT_TIMESTAMP',
    'D3A_COUNT.EXTRACT',
    'D3A_COUNT.INIT',
    'D3A_COUNT.MERGE',
    'D3A_COUNT.MERGE_PARTIAL',
    'D3A_COUNT.TO_HLL',
    'DATE',
    'DATETIME',
    'DATETIME_ADD',
    'DATETIME_BUCKET',
    'DATETIME_DIFF',
    'DATETIME_SUB',
    'DATETIME_TRUNC',
    'DATE_ADD',
    'DATE_BUCKET',
    'DATE_DIFF',
    'DATE_FROM_UNIX_DATE',
    'DATE_SUB',
    'DATE_TRUNC',
    'DENSE_RANK',
    'DESTINATION_NODE_ID',
    'DETERMINISTIC_DECRYPT_BYTES',
    'DETERMINISTIC_DECRYPT_STRING',
    'DETERMINISTIC_ENCRYPT',
    'DIV',
    'DOT_PRODUCT',
    'EDGES',
    'EDIT_DISTANCE',
    'ELEMENTWISE_AVG',
    'ELEMENTWISE_SUM',
    'ELEMENT_DEFINITION_NAME',
    'ELEMENT_ID',
    'ENDS_WITH',
    'ENUM_VALUE_DESCRIPTOR_PROTO',
    'ERROR',
    'EUCLIDEAN_DISTANCE',
    'EXP',
    'EXTRACT',
    'EXTRACT_FOR_DP_APPROX_COUNT_DISTINCT',
    'FARM_FINGERPRINT',
    'FILTER_FIELDS',
    'FIRST_VALUE',
    'FLATTEN',
    'FLOAT32',
    'FLOAT32_ARRAY',
    'FLOAT64',
    'FLOAT64_ARRAY',
    'FLOOR',
    'FORMAT',
    'FORMAT_DATE',
    'FORMAT_DATETIME',
    'FORMAT_TIME',
    'FORMAT_TIMESTAMP',
    'FROM_BASE32',
    'FROM_BASE64',
    'FROM_HEX',
    'GENERATE_ARRAY',
    'GENERATE_DATE_ARRAY',
    'GENERATE_RANGE_ARRAY',
    'GENERATE_TIMESTAMP_ARRAY',
    'GENERATE_UUID',
    'GREATEST',
    'GROUPING',
    'HLL_COUNT.EXTRACT',
    'HLL_COUNT.INIT',
    'HLL_COUNT.MERGE',
    'HLL_COUNT.MERGE_PARTIAL',
    'IEEE_DIVIDE',
    'IF',
    'IFERROR',
    'IFNULL',
    'IN UNNEST',
    'INITCAP',
    'INIT_FOR_DP_APPROX_COUNT_DISTINCT',
    'INSTR',
    'INT64',
    'INT64_ARRAY',
    'IS DESTINATION OF',
    'IS DISTINCT FROM',
    'IS NOT DISTINCT FROM',
    'IS SOURCE OF',
    'ISERROR',
    'IS_ACYCLIC',
    'IS_INF',
    'IS_NAN',
    'IS_SIMPLE',
    'IS_TRAIL',
    'JSON_ARRAY',
    'JSON_ARRAY_APPEND',
    'JSON_ARRAY_INSERT',
    'JSON_CONTAINS',
    'JSON_EXTRACT',
    'JSON_EXTRACT_ARRAY',
    'JSON_EXTRACT_SCALAR',
    'JSON_EXTRACT_STRING_ARRAY',
    'JSON_KEYS',
    'JSON_OBJECT',
    'JSON_QUERY',
    'JSON_QUERY_ARRAY',
    'JSON_REMOVE',
    'JSON_SET',
    'JSON_STRIP_NULLS',
    'JSON_TYPE',
    'JSON_VALUE',
    'JSON_VALUE_ARRAY',
    'JUSTIFY_DAYS',
    'JUSTIFY_HOURS',
    'JUSTIFY_INTERVAL',
    'KEYS.ADD_KEY_FROM_RAW_BYTES',
    'KEYS.KEYSET_CHAIN',
    'KEYS.KEYSET_FROM_JSON',
    'KEYS.KEYSET_LENGTH',
    'KEYS.KEYSET_TO_JSON',
    'KEYS.NEW_KEYSET',
    'KEYS.NEW_WRAPPED_KEYSET',
    'KEYS.REWRAP_KEYSET',
    'KEYS.ROTATE_KEYSET',
    'KEYS.ROTATE_WRAPPED_KEYSET',
    'KLL_QUANTILES.EXTRACT_FLOAT64',
    'KLL_QUANTILES.EXTRACT_INT64',
    'KLL_QUANTILES.EXTRACT_POINT_FLOAT64',
    'KLL_QUANTILES.EXTRACT_POINT_INT64',
    'KLL_QUANTILES.INIT_FLOAT64',
    'KLL_QUANTILES.INIT_INT64',
    'KLL_QUANTILES.MERGE_FLOAT64',
    'KLL_QUANTILES.MERGE_INT64',
    'KLL_QUANTILES.MERGE_PARTIAL',
    'KLL_QUANTILES.MERGE_POINT_FLOAT64',
    'KLL_QUANTILES.MERGE_POINT_INT64',
    'L1_NORM',
    'L2_NORM',
    'LABELS',
    'LAG',
    'LAST_DAY',
    'LAST_VALUE',
    'LAX_BOOL',
    'LAX_BOOL_ARRAY',
    'LAX_FLOAT32',
    'LAX_FLOAT32_ARRAY',
    'LAX_FLOAT64',
    'LAX_FLOAT64_ARRAY',
    'LAX_INT64',
    'LAX_INT64_ARRAY',
    'LAX_STRING',
    'LAX_STRING_ARRAY',
    'LEAD',
    'LEAST',
    'LEFT',
    'LENGTH',
    'LIKE ALL',
    'LIKE ALL UNNEST',
    'LIKE ANY',
    'LIKE ANY UNNEST',
    'LN',
    'LOG',
    'LOG10',
    'LOGICAL_AND',
    'LOGICAL_OR',
    'LOWER',
    'LPAD',
    'LTRIM',
    'MAKE_INTERVAL',
    'MANHATTAN_DISTANCE',
    'MAP_CARDINALITY',
    'MAP_CONTAINS_KEY',
    'MAP_DELETE',
    'MAP_EMPTY',
    'MAP_ENTRIES_SORTED',
    'MAP_ENTRIES_UNSORTED',
    'MAP_FILTER',
    'MAP_FROM_ARRAY',
    'MAP_GET',
    'MAP_INSERT',
    'MAP_INSERT_OR_REPLACE',
    'MAP_KEYS_SORTED',
    'MAP_KEYS_UNSORTED',
    'MAP_REPLACE',
    'MAP_VALUES_SORTED',
    'MAP_VALUES_SORTED_BY_KEY',
    'MAP_VALUES_UNSORTED',
    'MAX',
    'MD5',
    'MERGE_PARTIAL_FOR_DP_APPROX_COUNT_DISTINCT',
    'MIN',
    'MOD',
    'NET.HOST',
    'NET.IPV4_FROM_INT64',
    'NET.IPV4_TO_INT64',
    'NET.IP_FROM_STRING',
    'NET.IP_NET_MASK',
    'NET.IP_TO_STRING',
    'NET.IP_TRUNC',
    'NET.PUBLIC_SUFFIX',
    'NET.REG_DOMAIN',
    'NET.SAFE_IP_FROM_STRING',
    'NEW_UUID',
    'NODES',
    'NORMALIZE',
    'NORMALIZE_AND_CASEFOLD',
    'NOT LIKE ALL',
    'NOT LIKE ALL UNNEST',
    'NOT LIKE ANY',
    'NOT LIKE ANY UNNEST',
    'NTH_VALUE',
    'NTILE',
    'NULLIF',
    'NULLIFERROR',
    'NULLIFZERO',
    'OCTET_LENGTH',
    'OFFSET',
    'ORDINAL',
    'PARSE_BIGNUMERIC',
    'PARSE_DATE',
    'PARSE_DATETIME',
    'PARSE_JSON',
    'PARSE_NUMERIC',
    'PARSE_TIME',
    'PARSE_TIMESTAMP',
    'PATH',
    'PATH_FIRST',
    'PATH_LAST',
    'PATH_LENGTH',
    'PERCENTILE_CONT',
    'PERCENTILE_DISC',
    'PERCENT_RANK',
    'PI',
    'PIVOT',
    'PI_BIGNUMERIC',
    'PI_NUMERIC',
    'POW',
    'POWER',
    'PROPERTY_EXISTS',
    'PROPERTY_NAMES',
    'PROTO_MAP_CONTAINS_KEY',
    'PROTO_MODIFY_MAP',
    'RAND',
    'RANGE',
    'RANGE_BUCKET',
    'RANGE_CONTAINS',
    'RANGE_END',
    'RANGE_INTERSECT',
    'RANGE_IS_END_UNBOUNDED',
    'RANGE_IS_START_UNBOUNDED',
    'RANGE_OVERLAPS',
    'RANGE_START',
    'RANK',
    'REGEXP_CONTAINS',
    'REGEXP_EXTRACT',
    'REGEXP_EXTRACT_ALL',
    'REGEXP_INSTR',
    'REGEXP_REPLACE',
    'REGEXP_SUBSTR',
    'REPEAT',
    'REPLACE',
    'REVERSE',
    'RIGHT',
    'ROUND',
    'ROW_NUMBER',
    'RPAD',
    'RTRIM',
    'S2_CELLIDFROMPOINT',
    'S2_COVERINGCELLIDS',
    'SAFE_ADD',
    'SAFE_CONVERT_BYTES_TO_STRING',
    'SAFE_DIVIDE',
    'SAFE_MULTIPLY',
    'SAFE_NEGATE',
    'SAFE_OFFSET',
    'SAFE_ORDINAL',
    'SAFE_SUBTRACT',
    'SAFE_TO_JSON',
    'SAME',
    'SEC',
    'SECH',
    'SESSION_USER',
    'SHA1',
    'SHA256',
    'SHA512',
    'SIGN',
    'SIN',
    'SINH',
    'SOUNDEX',
    'SOURCE_NODE_ID',
    'SPLIT',
    'SPLIT_SUBSTR',
    'SQRT',
    'STARTS_WITH',
    'STDDEV',
    'STDDEV_POP',
    'STDDEV_SAMP',
    'STRING',
    'STRING_AGG',
    'STRING_ARRAY',
    'STRPOS',
    'ST_ANGLE',
    'ST_AREA',
    'ST_ASBINARY',
    'ST_ASGEOJSON',
    'ST_ASKML',
    'ST_ASTEXT',
    'ST_AZIMUTH',
    'ST_BOUNDARY',
    'ST_BOUNDINGBOX',
    'ST_BUFFER',
    'ST_BUFFERWITHTOLERANCE',
    'ST_CENTROID',
    'ST_CENTROID_AGG',
    'ST_CLOSESTPOINT',
    'ST_CLUSTERDBSCAN',
    'ST_CONTAINS',
    'ST_CONVEXHULL',
    'ST_COVEREDBY',
    'ST_COVERS',
    'ST_DIFFERENCE',
    'ST_DIMENSION',
    'ST_DISJOINT',
    'ST_DISTANCE',
    'ST_DUMP',
    'ST_DUMPPOINTS',
    'ST_DWITHIN',
    'ST_ENDPOINT',
    'ST_EQUALS',
    'ST_EXTENT',
    'ST_EXTERIORRING',
    'ST_GEOGFROM',
    'ST_GEOGFROMGEOJSON',
    'ST_GEOGFROMKML',
    'ST_GEOGFROMTEXT',
    'ST_GEOGFROMWKB',
    'ST_GEOGPOINT',
    'ST_GEOGPOINTFROMGEOHASH',
    'ST_GEOHASH',
    'ST_GEOMETRYTYPE',
    'ST_HAUSDORFFDISTANCE',
    'ST_HAUSDORFFDWITHIN',
    'ST_INTERIORRINGS',
    'ST_INTERSECTION',
    'ST_INTERSECTS',
    'ST_INTERSECTSBOX',
    'ST_ISCLOSED',
    'ST_ISCOLLECTION',
    'ST_ISEMPTY',
    'ST_ISRING',
    'ST_LENGTH',
    'ST_LINEINTERPOLATEPOINT',
    'ST_LINELOCATEPOINT',
    'ST_LINESUBSTRING',
    'ST_MAKELINE',
    'ST_MAKEPOLYGON',
    'ST_MAKEPOLYGONORIENTED',
    'ST_MAXDISTANCE',
    'ST_NEAREST_NEIGHBORS',
    'ST_NPOINTS',
    'ST_NUMGEOMETRIES',
    'ST_NUMPOINTS',
    'ST_PERIMETER',
    'ST_POINTN',
    'ST_SIMPLIFY',
    'ST_SNAPTOGRID',
    'ST_STARTPOINT',
    'ST_TOUCHES',
    'ST_UNARYUNION',
    'ST_UNION',
    'ST_UNION_AGG',
    'ST_WITHIN',
    'ST_X',
    'ST_Y',
    'SUBSTR',
    'SUBSTRING',
    'SUM',
    'TAN',
    'TANH',
    'TIME',
    'TIMESTAMP',
    'TIMESTAMP_ADD',
    'TIMESTAMP_BUCKET',
    'TIMESTAMP_DIFF',
    'TIMESTAMP_FROM_UNIX_MICROS',
    'TIMESTAMP_FROM_UNIX_MILLIS',
    'TIMESTAMP_FROM_UNIX_SECONDS',
    'TIMESTAMP_MICROS',
    'TIMESTAMP_MILLIS',
    'TIMESTAMP_SECONDS',
    'TIMESTAMP_SUB',
    'TIMESTAMP_TRUNC',
    'TIME_ADD',
    'TIME_DIFF',
    'TIME_SUB',
    'TIME_TRUNC',
    'TO_BASE32',
    'TO_BASE64',
    'TO_CODE_POINTS',
    'TO_HEX',
    'TO_JSON',
    'TO_JSON_STRING',
    'TRANSLATE',
    'TRIM',
    'TRUNC',
    'TYPEOF',
    'UNICODE',
    'UNIX_DATE',
    'UNIX_MICROS',
    'UNIX_MILLIS',
    'UNIX_SECONDS',
    'UNNEST',
    'UNPIVOT',
    'UPPER',
    'VARIANCE',
    'VAR_POP',
    'VAR_SAMP',
    'ZEROIFNULL',
]

keywords = [
    'ABORT',
    'ACCESS',
    'ACTION',
    'ACYCLIC',
    'ADD',
    'AFTER',
    'AGGREGATE',
    'ALL',
    'ALTER',
    'ALWAYS',
    'ANALYZE',
    'AND',
    'ANY',
    'APPROX',
    'ARE',
    'AS',
    'ASC',
    'ASCENDING',
    'ASSERT',
    'ASSERT_ROWS_MODIFIED',
    'AT',
    'BATCH',
    'BEGIN',
    'BETWEEN',
    'BIGDECIMAL',
    'BREAK',
    'BY',
    'CALL',
    'CASCADE',
    'CASE',
    'CAST',
    'CHECK',
    'CLAMPED',
    'CLONE',
    'CLUSTER',
    'COLLATE',
    'COLUMN',
    'COLUMNS',
    'COMMIT',
    'CONFLICT',
    'CONNECTION',
    'CONSTANT',
    'CONSTRAINT',
    'CONTAINS',
    'CONTINUE',
    'COPY',
    'CORRESPONDING',
    'CREATE',
    'CROSS',
    'CUBE',
    'CURRENT',
    'CYCLE',
    'DATA',
    'DATABASE',
    'DAY',
    'DAYOFWEEK',
    'DAYOFYEAR',
    'DECIMAL',
    'DECLARE',
    'DEFAULT',
    'DEFINE',
    'DEFINER',
    'DELETE',
    'DELETION',
    'DEPTH',
    'DESC',
    'DESCENDING',
    'DESCRIBE',
    'DESCRIPTOR',
    'DESTINATION',
    'DETERMINISTIC',
    'DISTINCT',
    'DO',
    'DROP',
    'EDGE',
    'ELSE',
    'ELSEIF',
    'END',
    'ENFORCED',
    'ERROR',
    'ESCAPE',
    'EXCEPT',
    'EXCEPTION',
    'EXCLUDE',
    'EXECUTE',
    'EXISTS',
    'EXPLAIN',
    'EXPORT',
    'EXTEND',
    'EXTERNAL',
    'EXTRACT',
    'FALSE',
    'FETCH',
    'FIELD',
    'FILES',
    'FILL',
    'FILTER',
    'FIRST',
    'FOLLOWING',
    'FOR',
    'FOREIGN',
    'FORK',
    'FORMAT',
    'FRIDAY',
    'FROM',
    'FULL',
    'FUNCTION',
    'GENERATED',
    'GRANT',
    'GRAPH',
    'GRAPH_TABLE',
    'GROUP',
    'GROUPING',
    'GROUPS',
    'GROUP_ROWS',
    'HAS',
    'HASH',
    'HAVING',
    'HIDDEN',
    'HOUR',
    'IDENTITY',
    'IF',
    'IGNORE',
    'IMMEDIATE',
    'IMMUTABLE',
    'IMPORT',
    'IN',
    'INCLUDE',
    'INCREMENT',
    'INDEX',
    'INNER',
    'INOUT',
    'INPUT',
    'INSERT',
    'INTERLEAVE',
    'INTERSECT',
    'INTO',
    'INVOKER',
    'IS',
    'ISOLATION',
    'ISOWEEK ',
    'ISOYEAR',
    'ITERATE',
    'JOIN',
    'KEY',
    'LABEL',
    'LABELED',
    'LANGUAGE',
    'LAST',
    'LATERAL',
    'LEAVE',
    'LEFT',
    'LET',
    'LEVEL',
    'LIKE',
    'LIMIT',
    'LOAD',
    'LOG',
    'LOOKUP',
    'LOOP',
    'MACRO',
    'MATCH',
    'MATCHED',
    'MATCH_RECOGNIZE',
    'MATERIALIZED',
    'MAX',
    'MAXVALUE',
    'MEASURES',
    'MERGE',
    'MESSAGE',
    'METADATA',
    'MICROSECOND',
    'MILLISECOND',
    'MIN',
    'MINUTE',
    'MINVALUE',
    'MODEL',
    'MODULE',
    'MONDAY',
    'MONTH',
    'NAME',
    'NANOSECOND',
    'NATURAL',
    'NEW',
    'NEXT',
    'NO',
    'NODE',
    'NOT',
    'NOTHING',
    'NULL',
    'NULLS',
    'NULL_FILTERED',
    'OF',
    'OFFSET',
    'ON',
    'ONEOF_CASE',
    'ONLY',
    'OPTIONAL',
    'OPTIONS',
    'OR',
    'ORDER',
    'OUT',
    'OUTER',
    'OUTPUT',
    'OVER',
    'OVERWRITE',
    'PARENT',
    'PARTITION',
    'PARTITIONS',
    'PAST',
    'PATH',
    'PATHS',
    'PATTERN',
    'PERCENT',
    'PIVOT',
    'POLICIES',
    'POLICY',
    'PRECEDING',
    'PRIMARY',
    'PRIVATE',
    'PRIVILEGE',
    'PRIVILEGES',
    'PROCEDURE',
    'PROJECT',
    'PROPERTIES',
    'PROPERTY',
    'PUBLIC',
    'QUALIFY',
    'QUARTER',
    'RAISE',
    'RAW',
    'READ',
    'RECURSIVE',
    'REFERENCES',
    'REMOTE',
    'REMOVE',
    'RENAME',
    'REPEAT',
    'REPEATABLE',
    'REPLACE',
    'REPLACE_FIELDS',
    'REPLICA',
    'REPORT',
    'RESPECT',
    'RESTRICT',
    'RESTRICTION',
    'RETURN',
    'RETURNS',
    'REVOKE',
    'RIGHT',
    'ROLLBACK',
    'ROLLUP',
    'ROW',
    'ROWS',
    'RUN',
    'SAFE_CAST',
    'SATURDAY',
    'SCHEMA',
    'SEARCH',
    'SECOND ',
    'SECURITY',
    'SELECT',
    'SEQUENCE',
    'SET',
    'SETS',
    'SHORTEST',
    'SHOW',
    'SIMPLE',
    'SKIP',
    'SNAPSHOT',
    'SOME',
    'SOURCE',
    'SQL',
    'STABLE',
    'START',
    'STATIC_DESCRIBE',
    'STORED',
    'STORING',
    'STRICT',
    'SUNDAY',
    'SYSTEM',
    'SYSTEM_TIME',
    'TABLE',
    'TABLES',
    'TABLESAMPLE',
    'TARGET',
    'TEMP',
    'TEMPORARY',
    'THEN',
    'THURSDAY',
    'TO',
    'TRAIL',
    'TRANSACTION',
    'TRANSFORM',
    'TREAT',
    'TRUE',
    'TRUNCATE',
    'TUESDAY',
    'TYPE',
    'UNBOUNDED',
    'UNDROP',
    'UNION',
    'UNIQUE',
    'UNKNOWN',
    'UNNEST',
    'UNPIVOT',
    'UNTIL',
    'UPDATE',
    'USING',
    'VALUE',
    'VALUES',
    'VECTOR',
    'VIEW',
    'VIEWS',
    'VOLATILE',
    'WALK',
    'WEDNESDAY',
    'WEEK',
    'WEIGHT',
    'WHEN',
    'WHERE',
    'WHILE',
    'WINDOW',
    'WITH',
    'WITHIN',
    'WRITE',
    'YEAR',
    'ZONE',
]

operators = [
    '!=',
    '&',
    '*',
    '+',
    '-',
    '/',
    '<',
    '<<',
    '<=',
    '=',
    '>',
    '>=',
    '>>',
    '^',
    '|',
    '||',
    '~',
]

types = [
    'ARRAY',
    'BIGNUMERIC',
    'BOOL',
    'BYTES',
    'DATE',
    'DATETIME',
    'DOUBLE',
    'ENUM',
    'EXTENDED',
    'FLOAT',
    'GEOGRAPHY',
    'GRAPH_ELEMENT',
    'GRAPH_PATH',
    'INT32',
    'INT64',
    'INTERVAL',
    'JSON',
    'MAP',
    'MEASURE',
    'NUMERIC',
    'PROTO',
    'RANGE',
    'STRING',
    'STRUCT',
    'TIME',
    'TIMESTAMP',
    'TIMESTAMP_PICOS',
    'TOKENLIST',
    'UINT32',
    'UINT64',
    'UUID',
]
