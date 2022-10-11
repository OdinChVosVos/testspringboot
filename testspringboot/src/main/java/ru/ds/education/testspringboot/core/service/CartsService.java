package ru.ds.education.testspringboot.core.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.ds.education.testspringboot.core.mapper.CartsMapper;
import ru.ds.education.testspringboot.core.model.CartsDto;
import ru.ds.education.testspringboot.core.model.TovarDto;
import ru.ds.education.testspringboot.core.model.TrashDto;
import ru.ds.education.testspringboot.db.entity.Carts;
import ru.ds.education.testspringboot.db.entity.Category;
import ru.ds.education.testspringboot.db.entity.Tovar;
import ru.ds.education.testspringboot.db.entity.Trash;
import ru.ds.education.testspringboot.db.repository.CartsRepository;


@Service
public class CartsService {

    @Autowired
    private CartsRepository cartsRepository;

    @Autowired
    private CartsMapper cartsMapper;

    @Autowired
    private TrashService trashService;

    public void addToCart(Long id, TrashDto tovar){
        if (cartsRepository.getLastId(id) == null)
            cartsRepository.add(id);
        Long cartId = cartsRepository.getLastId(id);
        trashService.addToCart(tovar, cartId);
    }

}
