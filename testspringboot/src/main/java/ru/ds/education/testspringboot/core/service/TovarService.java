package ru.ds.education.testspringboot.core.service;

import org.springframework.beans.BeanUtils;
import org.springframework.beans.BeanWrapper;
import org.springframework.beans.BeanWrapperImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.ds.education.testspringboot.core.model.TovarDto;
import ru.ds.education.testspringboot.db.entity.Category;
import ru.ds.education.testspringboot.db.entity.Tovar;
import ru.ds.education.testspringboot.db.repository.TovarRepository;
import ru.ds.education.testspringboot.core.mapper.TovarMapper;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Service
public class TovarService {

    @Autowired
    private TovarRepository tovarRepository;

    @Autowired
    private TovarMapper tovarMapper;

    @Autowired
    private RemindService remindService;


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

    public List<TovarDto> putGoods(List<TovarDto> goods){
        List<TovarDto> newGoods = new ArrayList<>();

        for (TovarDto good:goods) {
            Tovar existingTovar = tovarRepository.getById(good.getId());
            BeanUtils.copyProperties(good, existingTovar, getNullPropertyNames(good));
            newGoods.add(tovarMapper.map(tovarRepository.saveAndFlush(existingTovar), TovarDto.class));
        }
        remindService.check();
        return newGoods;

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


    private String[] getNullPropertyNames (Object source) {
        final BeanWrapper src = new BeanWrapperImpl(source);
        java.beans.PropertyDescriptor[] pds = src.getPropertyDescriptors();
        List<String> emptyNames = new ArrayList<>();
        emptyNames.add("id");
        for(java.beans.PropertyDescriptor pd : pds) {
            Object srcValue = src.getPropertyValue(pd.getName());
            if (srcValue == null) emptyNames.add(pd.getName());
        }
        String[] result = new String[emptyNames.size()];
        return emptyNames.toArray(result);
    }


}
