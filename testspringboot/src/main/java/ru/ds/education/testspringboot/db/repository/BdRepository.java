package ru.ds.education.testspringboot.db.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import org.springframework.stereotype.Repository;

import ru.ds.education.testspringboot.db.entity.Bd;
import ru.ds.education.testspringboot.db.entity.Journal;

import java.util.List;


@Repository
public interface BdRepository extends JpaRepository<Bd, Long> {

    @Query(value = "Select en from Bd en where en.login = :login")
    Bd findByLogin(@Param("login") String login);

    @Query(value = "Select en from Bd en where en.achieves = :achieves")
    List<Bd> findByAchieves(@Param("achieves") int achieves);

    @Query(value = "Select en from Bd en where en.status = :status")
    List<Bd> findByStatus(@Param("status") int status);

    @Query(value = "Select en.id from Bd en")
    List<Long> getAllid();

}
