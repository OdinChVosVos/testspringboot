package ru.ds.education.testspringboot.api.controller;


import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import ru.ds.education.testspringboot.api.job.ParseTask;
import ru.ds.education.testspringboot.core.model.TovarDto;
import ru.ds.education.testspringboot.core.service.TovarService;


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

}
