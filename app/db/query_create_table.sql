create table plant
(
    id              int auto_increment primary key,
    name            varchar(50)                         null,
    temperature     float                               null,
    humidity        float                               null,
    light_intensity float                               null,
    soil_moisture   float                               null,
    status          varchar(50)                         null,
    time            timestamp default CURRENT_TIMESTAMP not null
);