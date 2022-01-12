package ru.ds.education.testspringboot.api.controller;

import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ru.ds.education.testspringboot.core.model.BdDto;
import ru.ds.education.testspringboot.core.model.JournalDto;
import ru.ds.education.testspringboot.core.service.JournalService;

import java.util.List;

@RestController
@RequestMapping("/api/journal")
public class JournalController {

    @Autowired
    private JournalService journalService;


    @ApiOperation(
            value = "Добавление записи в журнал входов и добавление соответствующего пользователя"
    )
    @PostMapping
    public JournalDto addEntry(@RequestBody JournalDto journal){
        return journalService.addEntry(journal);
    }


    @ApiOperation(
            value = "Получение информации о входе по номеру id входа"
    )
    @RequestMapping(value = {"{id}"}, method = RequestMethod.GET)
    public JournalDto getEntry(@PathVariable("id") Long id){
        return journalService.getEntry(id);
    }


    @ApiOperation(
            value = "Получение списка записей входов по количеству попаданий"
    )
    @GetMapping
    public List<JournalDto> getByPopad(@RequestParam int popad){
        return journalService.getByPopad(popad);
    }


    @ApiOperation(
            value = "Удаление записи входа"
    )
    @DeleteMapping(value = "/remove/entry/{id}")
    public ResponseEntity<Void> removeEntry(@PathVariable Long id){
        journalService.removeEntry(id);
        return ResponseEntity.noContent().build();
    }


    @ApiOperation(
            value = "Изменение записи входа по id"
    )
    @RequestMapping(value = "/update/id/{id}", method = RequestMethod.PUT)
    public ResponseEntity<JournalDto> updateEntry(@PathVariable Long id, @RequestBody JournalDto entry)
    {
        JournalDto result = journalService.updateEntry(id, entry);
        return ResponseEntity.ok().body(result);
    }
}
