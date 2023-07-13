-- 1. Pasirinkite visus duomenis iš lentelės "DARBUOTOJAI":

SELECT * FROM DARBUOTOJAI;

-- 2. Pasirinkite visus duomenis iš stulpelio "GIMIMO_DATA" lentelėje "DARBUOTOJAI":

SELECT GIMIMO_DATA FROM DARBUOTOJAI;

-- 3. Pasirinkite visus duomenis iš stulpelių "VARDAS","PAVARDĖ", "PAREIGOS" lentelėje "DARBUOTOJAI":

SELECT VARDAS, PAVARDĖ, PAREIGOS FROM DARBUOTOJAI;

-- 4. Pasirinkite skirtingas reikšmes iš stulpelio "SKYRIUS_PAVADINIMAS" lentelėje "DARBUOTOJAI":

SELECT DISTINCT SKYRIUS_PAVADINIMAS FROM DARBUOTOJAI;

-- 5. Pasirinkite visus duomenis apie darbuotojus, kurie dirba Gamybos skyriuje:

SELECT * FROM DARBUOTOJAI WHERE SKYRIUS_PAVADINIMAS = 'Gamybos';

-- 6. Pasirinkite duomenis, kokią pareigą užima Giedrius:

SELECT PAREIGOS FROM DARBUOTOJAI WHERE VARDAS = 'Giedrius';

-- 7. Pasirinkite visus duomenis apie darbuotojus, kurių gimimo data yra 1986-09-19:

SELECT * FROM DARBUOTOJAI WHERE GIMIMO_DATA = '1986-09-19';

-- 8. Pasirinkite darbuotojų vardus, kurių pavardė yra Sabutis:

SELECT VARDAS FROM DARBUOTOJAI WHERE PAVARDĖ = 'Sabutis';

-- 9. Pasirinkite duomenis (vardą ir pavardę) apie programuotojus iš Gamybos skyriaus:

SELECT VARDAS, PAVARDĖ FROM DARBUOTOJAI WHERE PAREIGOS = 'Programuotojas' AND SKYRIUS_PAVADINIMAS = 'Gamybos';

-- 10. Įterpkite naują darbuotoją į lentelę "DARBUOTOJAI", užpildydami visus reikiamus laukus (vardą, pavardę, gimimo datą, pareigas, skyriaus pavadinimą):

INSERT INTO DARBUOTOJAI (VARDAS, PAVARDĖ, GIMIMO_DATA, PAREIGOS, SKYRIUS_PAVADINIMAS) 
VALUES ('NewName', 'NewSurname', 'YYYY-MM-DD', 'NewPosition', 'NewDepartment');

-- 11. Įterpkite naują darbuotoją į lentelę "DARBUOTOJAI", užpildydami tik laukus (vardą, pavardę, gimimo datą). Pareigas ir skyriaus pavadinimą palikite neužpildytus:

INSERT INTO DARBUOTOJAI (VARDAS, PAVARDĖ, GIMIMO_DATA) 
VALUES ('NewName', 'NewSurname', 'YYYY-MM-DD');

-- 12. Užpildykite likusius tuščius laukus "DARBUOTOJAI" lentelėje, jūsų prieš tai įterptame įraše. Priskirkite darbuotojui pareigas ir skyrių:

UPDATE DARBUOTOJAI SET PAREIGOS = 'NewPosition', SKYRIUS_PAVADINIMAS = 'NewDepartment' 
WHERE VARDAS = 'NewName' AND PAVARDĖ = 'NewSurname' AND GIMIMO_DATA = 'YYYY-MM-DD';

-- 13. Ištrinkite "DARBUOTOJAI" lentelės įrašą, kurio gimimo data yra tokia, kurią jūs sukūrėte:

DELETE FROM DARBUOTOJAI WHERE GIMIMO_DATA = 'YYYY-MM-DD';

-- 14. Įterpkite du darbuotojus, pavardė Antanaitis, kurių pareigos būtų "Programuotojas":

INSERT INTO DARBUOTOJAI (VARDAS, PAVARDĖ, PAREIGOS) 
VALUES ('Name1', 'Antanaitis', 'Programuotojas'), ('Name2', 'Antanaitis', 'Programuotojas');

-- 15. Atnaujinkite lentelę "DARBUOTOJAI" ir pakeiskite pareigas į "Testuotojas" visiems darbuotojams, kurių pavardė yra "Antanaitis".

UPDATE DARBUOTOJAI SET PAREIGOS = 'Testuotojas' WHERE PAVARDĖ = 'Antanaitis';

-- 16. Pasirinkite ir suskaičiuokite visus įrašus iš lentelės "DARBUOTOJAI", kur darbuotojo pareigos yra "Testuotojas". Tai duos mums bendrą darbuotojų, dirbančių kaip "Testuotojai", skaičių.

SELECT COUNT(*) FROM DARBUOTOJAI WHERE PAREIGOS = 'Testuotojas';
