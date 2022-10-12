package ru.ds.education.testspringboot.api.controller;

import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import ru.ds.education.testspringboot.core.model.UsersDto;
import ru.ds.education.testspringboot.core.service.UsersService;

import java.math.BigInteger;
import java.util.List;


@RestController
@RequestMapping("/api/users")
public class UsersController {

    @Autowired
    private UsersService usersService;


    @ApiOperation(
            value = "Добавление пользователя"
    )
    @PostMapping
    public UsersDto signUp(@RequestBody UsersDto user){
        return usersService.signUp(user);
    }

    @ApiOperation(
            value = "Получение всех пользователей"
    )
    @RequestMapping(value = "/get", method = RequestMethod.GET)
    public List<UsersDto> getAll(){
        return usersService.getAll();
    }

    @ApiOperation(
            value = "Получение пользователя по ТГ id"
    )
    @RequestMapping(value = "/get/tg/{id}", method = RequestMethod.GET)
    public UsersDto getByTgId(@PathVariable Long id){
        return usersService.getByTgId(id);
    }
}
