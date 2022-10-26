package ru.ds.education.testspringboot.core.model;

import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.web.multipart.MultipartFile;

@Getter
@Setter
@NoArgsConstructor
public class TovarDto {

    @ApiModelProperty("id товара")
    private Long id;

    @ApiModelProperty("Категория товара")
    private CategoryDto category;

    @ApiModelProperty("Название товара")
    private String name;

    @ApiModelProperty("Стоимость товара")
    private double cost;

    @ApiModelProperty("Количество товара")
    private double quantity_in_stock;

    @ApiModelProperty("Описание товара")
    private String description;

    @ApiModelProperty("Картинка товара")
    private byte[] photo;

}
