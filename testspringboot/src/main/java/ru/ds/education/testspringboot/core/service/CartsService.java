package ru.ds.education.testspringboot.core.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.TaskScheduler;
import org.springframework.stereotype.Service;
import ru.ds.education.testspringboot.api.job.MyTimerTask;
import ru.ds.education.testspringboot.core.mapper.CartsMapper;
import ru.ds.education.testspringboot.core.mapper.TovarMapper;
import ru.ds.education.testspringboot.core.mapper.TrashMapper;
import ru.ds.education.testspringboot.core.model.BookedDto;
import ru.ds.education.testspringboot.core.model.CartsDto;
import ru.ds.education.testspringboot.core.model.TovarDto;
import ru.ds.education.testspringboot.core.model.TrashDto;
import ru.ds.education.testspringboot.db.entity.*;
import ru.ds.education.testspringboot.db.repository.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;
import java.util.concurrent.TimeUnit;


@Service
public class CartsService {

    @Autowired
    private CartsRepository cartsRepository;

    @Autowired
    private UsersRepository usersRepository;

    @Autowired
    private BookedRepository bookedRepository;

    @Autowired
    private TovarRepository tovarRepository;

    @Autowired
    private CartsMapper cartsMapper;

    @Autowired
    private TrashService trashService;

    @Autowired
    private TrashRepository trashRepository;

    @Autowired
    private TrashMapper trashMapper;

    public List<TrashDto> getAll(Long tgId){
        Long idUser = usersRepository.getByTgID(tgId).getId();

        if (cartsRepository.getLastId(idUser) == null)
            return null;
        Long cartId = cartsRepository.getLastId(idUser);
        return trashMapper.mapAsList(trashService.getByCart(cartId), TrashDto.class);
    }

    public void addToCart(Long tgId, TrashDto tovar){
        Long idUser = usersRepository.getByTgID(tgId).getId();
        if (cartsRepository.getLastId(idUser) == null)
            cartsRepository.add(idUser);
        Long cartId = cartsRepository.getLastId(idUser);
        trashService.addToCart(tovar, cartId);
    }

    public int countPrice(Long tgId){
        List<TrashDto> goods = getAll(tgId);
        int price = 0;
        for (TrashDto good:goods)
            price += good.getQuantity() * good.getTovar().getCost();
        return price;
    }

    public void clearCart(Long tgId){
        Long cartId = cartsRepository.getLastId(usersRepository.getByTgID(tgId).getId());
        trashRepository.deleteByCart(cartId);
        cartsRepository.deleteById(cartId);
    }

    public void buy(Long tgId){
        Long idUser = usersRepository.getByTgID(tgId).getId();

        List<TrashDto> cart = getAll(idUser);

        for (TrashDto elem:cart) {
            tovarRepository.takeFromTovar(elem.getTovar().getQuantity_in_stock()-elem.getQuantity(),
                    elem.getTovar().getId()
            );
            bookedRepository.putInBooked(elem.getTovar().getId(), elem.getQuantity());
        }

    }

}
