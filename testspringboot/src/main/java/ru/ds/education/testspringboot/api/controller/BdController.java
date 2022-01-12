package ru.ds.education.testspringboot.api.controller;

import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Role;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ru.ds.education.testspringboot.core.model.BdDto;
import ru.ds.education.testspringboot.core.model.JournalDto;
import ru.ds.education.testspringboot.core.service.BdService;
import ru.ds.education.testspringboot.programm.Programm;

import java.util.List;


@RestController
@RequestMapping("/api/bd")
public class BdController {

    @Autowired
    private BdService bdService;


    @ApiOperation(
            value = "Добавление пользователя"
    )
    @PostMapping
    public BdDto addUser(@RequestBody BdDto user){
        return bdService.addUser(user);
    }


    @ApiOperation(
            value = "Удаление пользователя"
    )
    @DeleteMapping(value = "/remove/{id}")
    public ResponseEntity<Void> removeUser(@PathVariable Long id){
        bdService.removeUser(id);
        return ResponseEntity.noContent().build();
    }


    @ApiOperation(
            value = "Удаление пользователя по логину"
    )
    @DeleteMapping(value = "/remove/login/{login}")
    public ResponseEntity<Void> removeUserByLogin(@PathVariable String login){
        bdService.removeUserByLogin(login);
        return ResponseEntity.noContent().build();
    }


    @ApiOperation(
            value = "Изменение пользователя по id"
    )
    @RequestMapping(value = "/update/id/{id}", method = RequestMethod.PUT)
    public ResponseEntity<BdDto> updateUser(@PathVariable Long id, @RequestBody BdDto user)
    {
        BdDto result = bdService.updateUser(id, user);
        return ResponseEntity.ok().body(result);
    }


    @ApiOperation(
            value = "Запуск программы"
    )
    @RequestMapping(value = "/start", method = RequestMethod.GET)
    public String startPr()
    {
        bdService.startPr();
        return "Programm is shuted down.........";
    }


    @ApiOperation(
            value = "Получение списка пользователей по статусу"
    )
    @RequestMapping(value = "/getStatus", method = RequestMethod.GET)
    public List<BdDto> findByStatus(@RequestParam int status){
        return bdService.findByStatus(status);
    }


    @ApiOperation(
            value = "Получение списка пользователей по достижениям"
    )
    @RequestMapping(value = "/getAchieves", method = RequestMethod.GET)
    public List<BdDto> findByAchieves(@RequestParam int achieves){
        return bdService.findByAchieves(achieves);
    }

}
