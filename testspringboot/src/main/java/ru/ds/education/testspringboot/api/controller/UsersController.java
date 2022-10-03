package ru.ds.education.testspringboot.api.controller;

import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import ru.ds.education.testspringboot.core.model.UsersDto;
import ru.ds.education.testspringboot.core.service.UsersService;


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
}
