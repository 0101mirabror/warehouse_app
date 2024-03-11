CREATE TABLE `materials` (
  id integer PRIMARY KEY,
  `material_name` varchar(255)
);

CREATE TABLE `products` (
  `id` integer PRIMARY KEY,
  `product_name` varchar(255),
  `product_code` varchar(255)
);

CREATE TABLE `productmaterials` (
  `id` integer PRIMARY KEY,
  `product_id` integer,
  `material_id` integer,
  `quantity` integer
);

CREATE TABLE `warehouses` (
  `id` integer PRIMARY KEY,
  `material_id` integer,
  `remainder` integer,
  `price` integer
);

ALTER TABLE `productmaterials` ADD FOREIGN KEY (`product_id`) REFERENCES `products` (`id`);

ALTER TABLE `productmaterials` ADD FOREIGN KEY (`material_id`) REFERENCES `materials` (`id`);

ALTER TABLE `warehouses` ADD FOREIGN KEY (`material_id`) REFERENCES `materials` (`id`);
