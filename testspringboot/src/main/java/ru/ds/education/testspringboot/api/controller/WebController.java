package ru.ds.education.testspringboot.api.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;

import org.springframework.web.bind.annotation.RequestMethod;
import ru.ds.education.testspringboot.core.mapper.UsersMapper;
import ru.ds.education.testspringboot.core.model.UsersDto;
import ru.ds.education.testspringboot.core.service.UsersService;
import ru.ds.education.testspringboot.db.entity.Users;

@Controller
public class WebController {

    @Autowired
    private UsersService usersService;

    @Autowired
    private UsersMapper usersMapper;

    @GetMapping("/")
    public String index(){
        return "index";
    }

    @RequestMapping("/admin")
    public String admin(Model model){
        model.addAttribute("users", usersService.getAll());
        model.addAttribute("user", new UsersDto());
        return "admin";
    }

    @RequestMapping(value = { "/addUser" }, method = RequestMethod.POST)
    public String addUser(Model model, @ModelAttribute("user") UsersDto user) {
        usersService.signUp(user);
        return "redirect:/admin";
    }
}
