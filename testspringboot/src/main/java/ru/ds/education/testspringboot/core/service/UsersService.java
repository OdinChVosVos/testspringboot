package ru.ds.education.testspringboot.core.service;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.ds.education.testspringboot.core.model.UsersDto;
import ru.ds.education.testspringboot.db.entity.Users;
import ru.ds.education.testspringboot.core.mapper.UsersMapper;
import ru.ds.education.testspringboot.db.repository.UsersRepository;

import java.math.BigInteger;
import java.util.List;


@Service
public class UsersService {

    @Autowired
    private UsersRepository usersRepository;

    @Autowired
    private UsersMapper usersMapper;


    public UsersDto signUp(UsersDto user){
        Users newUser = usersMapper.map(user, Users.class);
        newUser = usersRepository.save(newUser);
        user = usersMapper.map(newUser, UsersDto.class);
        return user;
    }

    public List<UsersDto> getAll(){
        return usersMapper.mapAsList(usersRepository.findAll(), UsersDto.class);
    }

    public UsersDto getByTgId(Long id){
        return usersMapper.map(usersRepository.getByTgID(id), UsersDto.class);
    }

}
