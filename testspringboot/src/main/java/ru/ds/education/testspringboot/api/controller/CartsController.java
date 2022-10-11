package ru.ds.education.testspringboot.api.controller;

import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import ru.ds.education.testspringboot.core.model.CartsDto;
import ru.ds.education.testspringboot.core.model.TovarDto;
import ru.ds.education.testspringboot.core.model.TrashDto;
import ru.ds.education.testspringboot.core.service.CartsService;


@RestController
@RequestMapping("/api/carts")
public class CartsController {

    @Autowired
    private CartsService cartsService;


    @ApiOperation(
            value = "Добавление товара в корзину"
    )
    @RequestMapping(value = "/{id}", method = RequestMethod.POST)
    public void addToCart(@PathVariable Long id, @RequestBody TrashDto tovar){
        cartsService.addToCart(id, tovar);
    }

}