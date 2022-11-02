package ru.ds.education.testspringboot.api.controller;

import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import ru.ds.education.testspringboot.core.model.RemindDto;
import ru.ds.education.testspringboot.core.model.TovarDto;
import ru.ds.education.testspringboot.core.model.TrashDto;
import ru.ds.education.testspringboot.core.service.RemindService;

import java.util.List;

@RestController
@RequestMapping("/api/remind")
public class RemindController {

    @Autowired
    private RemindService remindService;


    @ApiOperation(
            value = "Добавление товара в список желаемого"
    )
    @RequestMapping(value = "/{id}", method = RequestMethod.POST)
    public void addToRemind(@PathVariable Long id,
                            @RequestBody TovarDto tovar,
                            @RequestParam int quantity)
    {
        remindService.addToRemind(id, tovar.getId(), quantity);
    }

    @ApiOperation(
            value = "Получение всех товаров из списка желаемого"
    )
    @RequestMapping(value = "/get/{id}", method = RequestMethod.GET)
    public List<RemindDto> getAll(@PathVariable Long id){
        return remindService.getAll(id);
    }

}