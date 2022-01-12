package ru.ds.education.testspringboot.core.service;


import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import ru.ds.education.testspringboot.core.model.BdDto;
import ru.ds.education.testspringboot.db.entity.Bd;
import ru.ds.education.testspringboot.exceptions.CanTEditHimException;
import ru.ds.education.testspringboot.exceptions.IHaveHimException;
import ru.ds.education.testspringboot.exceptions.NoRemoveException;
import ru.ds.education.testspringboot.exceptions.ThereIsNoSuchUserException;
import ru.ds.education.testspringboot.core.mapper.JournalMapper;
import ru.ds.education.testspringboot.core.model.JournalDto;
import ru.ds.education.testspringboot.db.entity.Journal;
import ru.ds.education.testspringboot.db.repository.JournalRepository;

import java.util.List;


@Service
public class JournalService {

    @Autowired
    private JournalRepository journalRepository;

    @Autowired
    private JournalMapper journalMapper;


    public JournalDto addEntry(JournalDto journal){
        try{
            Journal entryNew = journalMapper.map(journal, Journal.class);
            entryNew = journalRepository.save(entryNew);
            journal = journalMapper.map(entryNew, JournalDto.class);
            return journal;
        }
        catch(RuntimeException e) {
            throw new IHaveHimException();
        }
    }


    public JournalDto getEntry(Long id){
        try {
            Journal user = journalRepository.findById(id)
                    .orElseThrow(ThereIsNoSuchUserException::new);
            return journalMapper.map(user, JournalDto.class);
        }
        catch (RuntimeException e){
            throw new IHaveHimException();
        }
    }


    public List<JournalDto> getByPopad(int popad){
        try {
            List<Journal> entriesList = journalRepository.findByPopad(popad);
            if (entriesList.isEmpty()) {
                throw new ThereIsNoSuchUserException();
            }
            return journalMapper.mapAsList(entriesList, JournalDto.class);
        }
        catch(RuntimeException e){
            throw new IHaveHimException();
        }
    }


    public void removeEntry(Long id){
        try{
            journalRepository.deleteById(id);
        }
        catch (RuntimeException e){
            throw new NoRemoveException();
        }
    }


    public JournalDto updateEntry(Long id, JournalDto entry){
        try{
            Journal existingEntry = journalRepository.getById(id);
            BeanUtils.copyProperties(entry, existingEntry, "id");
            return journalMapper.map(journalRepository.saveAndFlush(existingEntry), JournalDto.class);
        }
        catch (RuntimeException e){
            throw new CanTEditHimException();
        }
    }

}
