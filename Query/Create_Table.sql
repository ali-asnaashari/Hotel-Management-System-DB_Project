-- T-1
CREATE TABLE Room_Type (
    room_type_id INTEGER AUTO_INCREMENT PRIMARY KEY ,
    no_beds      INTEGER NOT NULL ,
    description  TEXT NOT NULL ,
    image        BLOB NOT NULL
);

-- T-2
CREATE TABLE Room_Status (
	Room_Status_ID   INTEGER AUTO_INCREMENT PRIMARY KEY ,
	Room_Status_Name NVARCHAR(30) NOT NULL
);


-- T-3
CREATE TABLE Room (
	Room_ID             INTEGER AUTO_INCREMENT PRIMARY KEY ,
	Floor               INTEGER NOT NULL,
	Price_Per_Night     INTEGER NOT NULL,
	Maximum_Capacity    INTEGER NOT NULL,
	room_type_id        INTEGER NOT NULL,
	Room_Status_ID      INTEGER NOT NULL,
	FOREIGN KEY (room_type_id)   REFERENCES room_type(room_type_id),
	FOREIGN KEY (Room_Status_ID) REFERENCES room_status(Room_Status_ID)
);



-- T-4
CREATE TABLE Restaurant_CoffeeShop (
	Restaurant_CoffeeShop_ID             INTEGER AUTO_INCREMENT PRIMARY KEY ,
	Restaurant_CoffeeShop_Name           NVARCHAR(30) NOT NULL,
  Restaurant_CoffeeShop_Identifier     BIT NOT NULL
);


-- T-5
CREATE TABLE Food (
	Food_ID                     INTEGER AUTO_INCREMENT PRIMARY KEY ,
	Food_Name                   NVARCHAR(50) NOT NULL,
    Food_Price                  FLOAT NOT NULL,
    Food_Ingredients            Text NOT NULL,
    Food_Drink_Identifier       BIT NOT NULL,
    Restaurant_CoffeeShop_ID    INTEGER NOT NULL,
    FOREIGN KEY (Restaurant_CoffeeShop_ID) REFERENCES restaurant_coffeeshop(Restaurant_CoffeeShop_ID)
);


-- T-6
CREATE TABLE Food_Order (
	Food_Order_ID                     INTEGER AUTO_INCREMENT PRIMARY KEY ,
	Food_Order_Room_Rest              BIT(50) NOT NULL,
    Reservation_Details_ID    INTEGER NOT NULL,
    FOREIGN KEY (Reservation_Details_ID) REFERENCES reservation_details(Reservation_Details_ID)
);


-- T-7
CREATE TABLE Staff_Information (
	Staff_ID                     INTEGER AUTO_INCREMENT PRIMARY KEY ,
	Staff_Firstname              NVARCHAR(20) NOT NULL,
	Staff_Lastname               NVARCHAR(50) NOT NULL,
	Staff_Password               CHAR    (10) NOT NULL,
	Staff_Email                  VARCHAR (50) NOT NULL,
	Staff_National_ID            CHAR    (10) NOT NULL,
	Staff_Salary                 DECIMAL (9,2)NOT NULL,
	Staff_StartDate              DATE         NOT NULL,
	Staff_Role_Recep_Cleaning    BIT          NOT NULL
);

-- T-8
CREATE TABLE Booking_Status (
	Booking_Status_ID                INTEGER AUTO_INCREMENT PRIMARY KEY ,
	Booking_Status_name              NVARCHAR(20) NOT NULL
);


-- T-9
CREATE TABLE Guest (
	Guest_ID                INTEGER AUTO_INCREMENT PRIMARY KEY ,
	Guest_Firstname         NVARCHAR(20) NOT NULL,
	Guest_Lastname          NVARCHAR(50) NOT NULL,
	Guest_Password          CHAR    (10) NOT NULL,
	Guest_PhoneNumber       CHAR    (11) NOT NULL,
	Guest_Address           TEXT    NOT NULL,
	Guest_BirthDate         DATE    NOT NULL,
	Guest_Gender            BIT NOT NULL,
	Guest_National_ID       CHAR    (10) NOT NULL
);


-- T-10
CREATE TABLE Reservation (
	Reservation_ID                         INTEGER AUTO_INCREMENT PRIMARY KEY ,
	Reservation_Date                       DATE    NOT NULL,
	Reservation_no_night                   INTEGER NOT NULL,
	Reservation_CheckIn                    DATE    NOT NULL,
	Reservation_CheckOut                   DATE    NOT NULL,
	Reservation_Bill_Total_Amount          DECIMAL (9,2) NOT NULL,
	Reservation_Bill_Status_Paid_Unpaid    BIT     NOT NULL,

	Staff_ID                               INTEGER NOT NULL,
    FOREIGN KEY (Staff_ID)          REFERENCES staff_information(Staff_ID),
    Booking_Status_ID                      INTEGER NOT NULL,
    FOREIGN KEY (Booking_Status_ID) REFERENCES Booking_Status(Booking_Status_ID),
    Guest_ID                               INTEGER NOT NULL,
    FOREIGN KEY (Guest_ID)          REFERENCES Guest(Guest_ID)
);

-- T-11
CREATE TABLE People (
	People_National_ID       CHAR    (10) PRIMARY KEY NOT NULL,
	People_Firstname         NVARCHAR(20) NOT NULL,
	People_Lastname          NVARCHAR(50) NOT NULL,
	People_Gender            BIT NOT NULL,

    Reservation_ID                               INTEGER NOT NULL,
    FOREIGN KEY (Reservation_ID)          REFERENCES Reservation(Reservation_ID)
);


-- T-12
CREATE TABLE Reservation_Details (
	Reservation_Details_ID                         INTEGER AUTO_INCREMENT PRIMARY KEY ,
	Reservation_Details_Rate                       INTEGER    NOT NULL,
	Reservation_Details_Extra_Facilities           TEXT    NOT NULL,

	Room_ID                               INTEGER NOT NULL,
    FOREIGN KEY (Room_ID)                 REFERENCES Room(Room_ID),
    Reservation_ID                        INTEGER NOT NULL,
    FOREIGN KEY (Reservation_ID)          REFERENCES Reservation(Reservation_ID)
);

-- T-13
CREATE TABLE Food_Contains (
	Food_Contains_ID                      INTEGER AUTO_INCREMENT PRIMARY KEY ,

	Food_ID                               INTEGER NOT NULL,
    FOREIGN KEY (Food_ID)                 REFERENCES Food(Food_ID),
    Food_Order_ID                        INTEGER NOT NULL,
    FOREIGN KEY (Food_Order_ID)          REFERENCES Food_Order(Food_Order_ID)
);

-- T-14
CREATE TABLE Cleaning_Service (
	Cleaning_Service_ID                   INTEGER AUTO_INCREMENT PRIMARY KEY ,
	Cleaning_Service_Time                 TIME NOT NULL ,
	Cleaning_Service_Date                 DATE NOT NULL ,
	Cleaning_Service_Description          TEXT NOT NULL ,

	Staff_ID                              INTEGER NOT NULL,
    FOREIGN KEY (Staff_ID)                REFERENCES Staff_Information(Staff_ID),
    Reservation_Details_ID                INTEGER NOT NULL,
    FOREIGN KEY (Reservation_Details_ID)  REFERENCES Reservation_Details(Reservation_Details_ID)
);