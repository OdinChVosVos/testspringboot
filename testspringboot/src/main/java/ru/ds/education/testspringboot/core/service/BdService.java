package ru.ds.education.testspringboot.core.service;

import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import ru.ds.education.testspringboot.exceptions.CanTEditHimException;
import ru.ds.education.testspringboot.exceptions.IHaveHimException;
import ru.ds.education.testspringboot.core.mapper.BdMapper;
import ru.ds.education.testspringboot.core.model.BdDto;
import ru.ds.education.testspringboot.db.entity.Bd;
import ru.ds.education.testspringboot.db.repository.BdRepository;
import ru.ds.education.testspringboot.exceptions.NoRemoveException;
import ru.ds.education.testspringboot.exceptions.ThereIsNoSuchUserException;
import ru.ds.education.testspringboot.programm.Programm;

import java.util.List;
import java.util.Objects;

@Service
public class BdService {

    @Autowired
    private BdRepository bdRepository;

    @Autowired
    private BdMapper bdMapper;


    public BdDto updateUser(Long id, BdDto user){
        try{
            if (id == 0) {
                throw new RuntimeException();
            }
            Bd existingUser = bdRepository.getById(id);
            BeanUtils.copyProperties(user, existingUser, "id");
            return bdMapper.map(bdRepository.saveAndFlush(existingUser), BdDto.class);
        }
        catch (RuntimeException e){
            throw new CanTEditHimException();
        }
    }


    public BdDto addUser(BdDto user){
        try{
            if (Objects.equals(user.getLogin(), "")){
                throw new RuntimeException();
            }
            if (user.getId() != null) {
                if (bdRepository.getAllid().contains(user.getId())){
                    throw new RuntimeException();
                }
            }
            Bd newUser = bdMapper.map(user, Bd.class);
            newUser = bdRepository.save(newUser);
            user = bdMapper.map(newUser, BdDto.class);
            return user;
        }
        catch (RuntimeException e){
            throw new IHaveHimException();
        }
    }


    public void removeUser(Long id){
        try{
            if (id == 0) {
                throw new RuntimeException();
            }
            bdRepository.deleteById(id);
        }
        catch (RuntimeException e){
            throw new NoRemoveException();
        }
    }


    public void removeUserByLogin(String login){
        try{
            if (Objects.equals(login, "admin")) {
                throw new RuntimeException();
            }
            Bd oldUser = bdRepository.findByLogin(login);
            bdRepository.delete(oldUser);
        }
        catch (RuntimeException e){
            throw new NoRemoveException();
        }
    }


    public List<BdDto> findByStatus(int status){
        try{
            List<Bd> usersList = bdRepository.findByStatus(status);
            if (usersList.isEmpty()){
                throw new RuntimeException();
            }
            return bdMapper.mapAsList(usersList, BdDto.class);
        }
        catch(RuntimeException e){
            throw new ThereIsNoSuchUserException();
        }
    }


    public List<BdDto> findByAchieves(int achieves){
        try{
            List<Bd> usersList = bdRepository.findByAchieves(achieves);
            if (usersList.isEmpty()){
                throw new RuntimeException();
            }
            return bdMapper.mapAsList(usersList, BdDto.class);
        }
        catch(RuntimeException e){
            throw new ThereIsNoSuchUserException();
        }
    }


    public void startPr(){
        new Programm().start();
    }
}
