package ru.ds.education.testspringboot.core.model;

import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
public class UsersDto {

    @ApiModelProperty("id пользователя")
    private Long id;

    @ApiModelProperty("Имя пользователя")
    private String name;

    @ApiModelProperty("Номер телефона")
    private String phone;

    @ApiModelProperty("Почта")
    private String mail;

    @ApiModelProperty("Соглашение на получение оповещений")
    private boolean agreement;

}
