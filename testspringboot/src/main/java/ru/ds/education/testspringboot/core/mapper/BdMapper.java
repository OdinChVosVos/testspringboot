package ru.ds.education.testspringboot.core.mapper;

import ma.glasnost.orika.MapperFactory;
import ma.glasnost.orika.impl.ConfigurableMapper;
import org.springframework.stereotype.Component;
import ru.ds.education.testspringboot.core.model.BdDto;
import ru.ds.education.testspringboot.db.entity.Bd;

@Component
public class BdMapper extends ConfigurableMapper {

    @Override
    protected void configure(MapperFactory factory) {
        factory.classMap(Bd.class, BdDto.class)
                .byDefault()
                .register();
    }
}
