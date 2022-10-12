package ru.ds.education.testspringboot.core.service;

import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.ds.education.testspringboot.core.model.TovarDto;
import ru.ds.education.testspringboot.db.entity.Category;
import ru.ds.education.testspringboot.db.entity.Tovar;
import ru.ds.education.testspringboot.db.repository.TovarRepository;
import ru.ds.education.testspringboot.core.mapper.TovarMapper;

import java.util.List;

@Service
public class TovarService {

    @Autowired
    private TovarRepository tovarRepository;

    @Autowired
    private TovarMapper tovarMapper;


    public TovarDto addTovar(TovarDto tovar){
        if (tovarRepository.getAllCategories().contains(tovar.getCategory().getName())){
            System.out.println("dwvw");

            Category category = tovarRepository.findCategory(tovar.getCategory().getName());
            tovarRepository.createTovar(
                    category.getId(), tovar.getName(),
                    tovar.getCost(), tovar.getQuantity_in_stock(),
                    tovar.getDescription(), tovar.getPhoto()
            );

            Tovar newTovar = new Tovar(tovarRepository.findIdAdded(category.getId()),
                    category,
                    tovar.getName(),
                    tovar.getCost(), tovar.getQuantity_in_stock(),
                    tovar.getDescription(), tovar.getPhoto()
            );

            return tovarMapper.map(newTovar, TovarDto.class);
        }
        else {
            Tovar newTovar = tovarMapper.map(tovar, Tovar.class);
            newTovar = tovarRepository.save(newTovar);
            tovar = tovarMapper.map(newTovar, TovarDto.class);
            return tovar;
        }
    }

    public List<TovarDto> getAll(){
        return tovarMapper.mapAsList(tovarRepository.findAll(), TovarDto.class);
    }

    public List<TovarDto> getCategory(int category){
        return tovarMapper.mapAsList(tovarRepository.findByCategory(category), TovarDto.class);
    }

    public TovarDto getTovar(Long id){
        return tovarMapper.map(tovarRepository.getById(id), TovarDto.class);
    }


}
