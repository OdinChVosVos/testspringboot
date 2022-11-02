package ru.ds.education.testspringboot.db.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;
import ru.ds.education.testspringboot.db.entity.Booked;
import ru.ds.education.testspringboot.db.entity.Tovar;

import javax.transaction.Transactional;

@Repository
public interface BookedRepository extends JpaRepository<Booked, Long> {

    @Modifying
    @Transactional
    @Query(value = "Insert into Booked VALUES (nextval('booked_seq'), :id_tovar, :booked_quantity);",
            nativeQuery = true)
    void putInBooked(
            @Param("id_tovar") Long id_tovar,
            @Param("booked_quantity") double booked_quantity
    );

}
