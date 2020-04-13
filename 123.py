#импортируем модули
import numpy as np 
import cv2 
  
cap = cv2.VideoCapture(0) #вызываем метод из cv2 возвращающий видео с первой камеры на компьютере 
  
fourcc = cv2.VideoWriter_fourcc(*'XVID') #выбираем кодек во время создания объекта записи
fps = 20.0
capture_size = (int(cap.get(3)), int(cap.get(4)))

out = cv2.VideoWriter('output.avi', fourcc, fps, capture_size) #прописываем доп аргументы для вывода видео
	
while(True): #бесконечный цикл захвата кадров и их обработки

	ret, frame = cap.read() #считываем кадр, и распаковываем, где frame - кадр, ret - boolean значение, если кадр был пойман успешно 
	if ret:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #конвертируем в серые цвета, принимая OCV как BGR
		out.write(gray) #записываем кадр(измененный) 

		cv2.imshow('Original', frame) #вызываем метод imshow для того чтобы отобразить окно и показать оригинальную картинку
	   
		cv2.imshow('Gray', gray) #тот же метод для отдельного окна, где мы показываем обработанные, серые кадры

		if cv2.waitKey(1) & 0xFF == ord('q'): #чтобы закончить запись, и выйти из цикла, мы используем хендлер ввода
			break
	else:
		break

cap.release() #заканчиваем работу с вебкамерой

out.release() #заканчиваем работу с записью

cv2.destroyAllWindows() #уничтожаем все окна, и освобождаем пямять для системы