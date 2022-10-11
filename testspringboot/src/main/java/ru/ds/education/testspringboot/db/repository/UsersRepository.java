package ru.ds.education.testspringboot.db.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;
import ru.ds.education.testspringboot.db.entity.Users;

import java.math.BigInteger;

@Repository
public interface UsersRepository extends JpaRepository<Users, Long> {

    @Query(value = "Select n from Users n where n.id_telegram = :id_telegram")
    Users getByTgID(@Param("id_telegram") Long id_telegram);

}
