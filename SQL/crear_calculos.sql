create table if not exists calculos_renta (
    id_calculo serial primary key not null,
    cedula_usuario varchar(20) not null,
    ingreso_bruto decimal not null,
    aportes_ley decimal not null,
    deducciones decimal not null,
    renta_liquida decimal not null,
    fecha_creacion date not null
);