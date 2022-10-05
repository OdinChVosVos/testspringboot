package ru.ds.education.testspringboot.api.controller;


import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import ru.ds.education.testspringboot.api.job.ParseTask;
import ru.ds.education.testspringboot.core.model.TovarDto;
import ru.ds.education.testspringboot.core.model.UsersDto;
import ru.ds.education.testspringboot.core.service.TovarService;

import java.util.List;


@RestController
@RequestMapping("/api/tovar")
public class TovarController {

    @Autowired
    private TovarService tovarService;

    @Autowired
    private ParseTask parseTask;


    @ApiOperation(
            value = "Добавление товаров"
    )
    @RequestMapping(value = "", method = RequestMethod.POST)
    public TovarDto addTovar(@RequestBody TovarDto tovar){
        return tovarService.addTovar(tovar);
    }


    @ApiOperation(
            value = "Добавление товаров(парсинг)"
    )
    @RequestMapping(value = "/parse", method = RequestMethod.GET)
    public String parseProducts(){
        return parseTask.parseProducts("mashiny");
    }


    @ApiOperation(
            value = "Получение всех товаров"
    )
    @RequestMapping(value = "/get", method = RequestMethod.GET)
    public List<TovarDto> getAll(){
        return tovarService.getAll();
    }


    @ApiOperation(
            value = "Получение товара по id"
    )
    @RequestMapping(value = "/get/{id}", method = RequestMethod.GET)
    public TovarDto getTovar(@PathVariable Long id){
        return tovarService.getTovar(id);
    }


    @ApiOperation(
            value = "Получение товаров в категории"
    )
    @RequestMapping(value = "/get/category/{category}", method = RequestMethod.GET)
    public List<TovarDto> getCategory(@PathVariable int category){
        return tovarService.getCategory(category);
    }


}
