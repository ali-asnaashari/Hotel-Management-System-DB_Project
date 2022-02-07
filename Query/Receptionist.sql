-- 1
SELECT Staff_Email,Staff_Password FROM staff_information
    WHERE Staff_Email = Input_Recep_Email AND Staff_Password = Input_Recep_Passwprd;

-- 2
SELECT Reservation_ID,Reservation_Date FROM reservation WHERE Booking_Status_ID = 1 ORDER BY Reservation_Date ASC;

-- 3

if(ConfirmButton.clicked()):
    UPDATE reservation SET Booking_Status_ID = 2,Staff_ID = Staff_ID_Variable_Saved
            WHERE Reservation_ID = Input_Reservation_ID;

else if(ConfirmButton.Cancel())
    UPDATE reservation SET Booking_Status_ID = 5,Staff_ID = Staff_ID_Variable_Saved
            WHERE Reservation_ID = Input_Reservation_ID;

-- 4
SELECT guest.Guest_ID,Guest_Firstname,Guest_Lastname,Guest_Address,Guest_BirthDate FROM
       guest JOIN reservation  ON guest.Guest_ID = reservation.Guest_ID;

-- 5
SELECT Room_ID,Room_Status_Name FROM room JOIN room_status on room_status.Room_Status_ID = room.Room_Status_ID;

SELECT Room_Status_Name,COUNT(Room_ID) FROM room JOIN room_status on room_status.Room_Status_ID = room.Room_Status_ID
    GROUP BY Room_Status_Name;

SELECT Room_ID FROM room JOIN room_status on room_status.Room_Status_ID = room.Room_Status_ID
    WHERE room.Room_Status_ID = 2;


-- 6
SELECT COUNT(Reservation_ID) FROM reservation
    JOIN booking_status ON reservation.Booking_Status_ID = booking_status.Booking_Status_ID
    WHERE reservation.Booking_Status_ID = 2 AND Reservation_Date BETWEEN Input_User_Date_One AND Input_User_Date_Two;

-- 7
SELECT Guest_Firstname,Guest_Lastname,Guest_BirthDate,Guest_National_ID
       FROM reservation JOIN guest ON reservation.Guest_ID = guest.Guest_ID
       WHERE Guest_BirthDate BETWEEN Reservation_CheckIn AND Reservation_CheckOut
       AND Reservation_CheckOut > DATE_TODAY_PYTHON;

-- 10
SELECT reservation.Reservation_ID,Cleaning_Service.* FROM reservation_details
       JOIN reservation       ON reservation_details.Reservation_ID = reservation.Reservation_ID
       JOIN cleaning_service  ON reservation_details.Reservation_Details_ID = cleaning_service.Reservation_Details_ID
       JOIN room              ON room.Room_ID = reservation_details.Room_ID
       WHERE reservation.Reservation_ID = Input_Reservation_ID;

-- 11
SELECT Staff_ID,Staff_Firstname,Staff_Lastname FROM staff_information WHERE Staff_Role_Recep_Cleaning = 0;
SELECT Cleaning_Service_ID FROM cleaning_service WHERE Staff_ID = -1;
UPDATE cleaning_service SET Staff_ID = Input_Staff_ID_User WHERE Cleaning_Service_ID = Input_Cleaning_Service_User;

