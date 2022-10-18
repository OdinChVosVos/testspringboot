package ru.ds.education.testspringboot.core.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.ds.education.testspringboot.core.mapper.TrashMapper;
import ru.ds.education.testspringboot.core.model.CartsDto;
import ru.ds.education.testspringboot.core.model.TovarDto;
import ru.ds.education.testspringboot.core.model.TrashDto;
import ru.ds.education.testspringboot.db.entity.Tovar;
import ru.ds.education.testspringboot.db.entity.Trash;
import ru.ds.education.testspringboot.db.repository.TrashRepository;

import java.util.ArrayList;
import java.util.List;

@Service
public class TrashService {

    @Autowired
    private TrashRepository trashRepository;

    @Autowired
    private TrashMapper trashMapper;

    public void addToCart(TrashDto tovar, Long cartId){
        trashRepository.add(tovar.getTovar().getId(), tovar.getQuantity(), cartId);
    }

    public ArrayList<Tovar> getByCart(Long cartId){
        List<Trash> oneCart = trashRepository.getByCart(cartId);
        ArrayList<Tovar> goods = new ArrayList<>();

        for (Trash good:oneCart)
            goods.add(good.getTovar());
        return goods;
    }

}