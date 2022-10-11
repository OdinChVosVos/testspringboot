package ru.ds.education.testspringboot.db.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;
import ru.ds.education.testspringboot.db.entity.Trash;

import javax.transaction.Transactional;

@Repository
public interface TrashRepository extends JpaRepository<Trash, Long> {


    @Modifying
    @Transactional
    @Query(value = "Insert into Trash VALUES (nextval('carts_seq'), :id_tovar, :quantity, :id_cart);", nativeQuery = true)
    void add(
            @Param("id_tovar") Long id_tovar,
            @Param("quantity") double quantity,
            @Param("id_cart") Long id_cart
    );

}