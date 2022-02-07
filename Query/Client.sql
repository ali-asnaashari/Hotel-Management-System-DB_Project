-- 1-REGISTER
-- INSERT INTO guest VALUES (4,'Mitra','Rahimi','1014256489','09185260443','Tehran','1999-10-27',0,'3214256687');

-- 1-LOGIN
-- SELECT Guest_National_ID,Guest_Password FROM guest
    -- WHERE Guest_National_ID = Input_NATIONAL_ID AND Guest_Password = Input_PASSWORD;

-- 2-SEARCH ROOM TYPE
-- SELECT R.*,RT.no_beds,RT.description,RT.image FROM room R
--   JOIN room_type RT ON R.room_type_id = RT.room_type_id WHERE RT.name = Input_Room_Type_name;


-- 3-ROOM RESERVED & ENTER PEOPLE DATA
-- user_id = SELECT Guest_ID FROM guest WHERE Guest_National_ID = Input_National_ID; -- UNIQUE
-- INSERT INTO reservation VALUES (1,'1400-10-8',2,'1400-10-10','1400-10-12',0.0,0,-1,1,3);
-- SELECT Reservation_ID FROM reservation WHERE reservation.Guest_ID = user_id; -- Not Unique --> Tuple(Len-1)
-- INSERT INTO reservation_details VALUES (1,0,'','Input_User','Reservation_ID');
-- INSERT INTO people VALUES ('1283404509','sara','Esi',0,1);

-- 4-5-6-View Restaurant OR CoffeeShop List + View Menu Restaurant OR CoffeeShop
-- Data = []
-- Data = SELECT Restaurant_CoffeeShop_ID,Restaurant_CoffeeShop_Name FROM restaurant_coffeeshop
--         WHERE Restaurant_CoffeeShop_Identifier = Input_RadioButton;

-- AFTER CLICK -> Visit Food Menu
-- Restaurant_Id,Restaurant_Name = Data[Click_Index-1]
-- SELECT Food_ID,Food_Name,Food_Price FROM food WHERE  food.Restaurant_CoffeeShop_ID = Restaurant_Id;

-- SEARCH FOOD NAME

-- SELECT Food_ID,Food_Name,Food_Price,Food_Ingredients FROM food
--    WHERE  food.Restaurant_CoffeeShop_ID = Restaurant_Id AND  Food_Name LIKE Input_Food_name ;

-- FOOD ORDER



-- 7-VIEW LIST OF FOOD ORDER --> Incomplete Guest ID
-- SELECT  Food_Contains.Food_Order_ID,Food_Contains.Food_ID,food.Food_Name,food.Food_Price FROM food_contains
--    JOIN Food ON food_contains.Food_ID = food.Food_ID
--    JOIN Food_order JOIN food_order fo on food_contains.Food_Order_ID = fo.Food_Order_ID;


-- 8-ORDER CLEANING ROOM
-- Reserve_Detail_Id,Room_Id,Reserv_id =
-- SELECT  reservation_details.Reservation_Details_ID,Room_ID,Reservation_ID FROM reservation_details
--    JOIN cleaning_service  on reservation_details.Reservation_Details_ID = cleaning_service.Reservation_Details_ID
--    JOIN staff_information on cleaning_service.Staff_ID = staff_information.Staff_ID;

-- INSERT INTO cleaning_service VALUES (1,Input_Time_User,Input_Date_User,'Complete',-1,Reserve_Detail_Id);

-- 9-View LIST RESERVATION
-- SELECT reservation.* FROM reservation WHERE Guest_ID = Input_Guest_id;


-- 10-View Bill account --> Enter Reservation ID
-- SELECT Reservation_Bill_Status_Paid_Unpaid,Reservation_Bill_Total_Amount FROM reservation
-- WHERE reservation = Input_reservation_id AND Guest_ID = Input_Guest_id;

-- Bill Account Details --> INCOMPLETE




