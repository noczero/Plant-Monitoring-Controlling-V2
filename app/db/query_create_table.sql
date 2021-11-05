create table plant
(
    id              bigint auto_increment primary key,
    name            varchar(50)                         null,
    temperature     float                               null,
    humidity        float                               null,
    light_intensity float                               null,
    soil_moisture   varchar(10)                         null,
    status          varchar(50)                         null,
    time            timestamp default CURRENT_TIMESTAMP not null
);