package ru.ds.education.testspringboot.api.controller;

import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import ru.ds.education.testspringboot.core.mapper.TovarMapper;
import ru.ds.education.testspringboot.core.model.CartsDto;
import ru.ds.education.testspringboot.core.model.TovarDto;
import ru.ds.education.testspringboot.core.model.TrashDto;
import ru.ds.education.testspringboot.core.service.CartsService;
import ru.ds.education.testspringboot.db.entity.Tovar;

import java.util.ArrayList;
import java.util.List;


@RestController
@RequestMapping("/api/carts")
public class CartsController {

    @Autowired
    private CartsService cartsService;


    @ApiOperation(
            value = "Получение всех товаров из корзины"
    )
    @RequestMapping(value = "/get/{id}", method = RequestMethod.GET)
    public List<TovarDto> getAll(@PathVariable Long id){
        return cartsService.getAll(id);
    }


    @ApiOperation(
            value = "Добавление товара в корзину"
    )
    @RequestMapping(value = "/{id}", method = RequestMethod.POST)
    public void addToCart(@PathVariable Long id, @RequestBody TrashDto tovar){
        cartsService.addToCart(id, tovar);
    }

}