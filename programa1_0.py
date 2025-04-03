import cv2

def ver_camara():
    cap = cv2.VideoCapture(1) #Abre la camara(0 para la camara predeterminada)

    if not cap.isOpened():
        print("error: no se pudo abrir la camara.")
        return
    
    while True:
        ret, frame=cap.read()#captura un frame de la camara
        if not  ret:
           print("error:no se pudo capturar el frame.")
           break

        cv2.imshow("camara en vivo", frame) #muestra el frame en una ventana

        #salir con la tecla 'q'
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break

    cap.release()#libera la camara
    cv2.destroyAllWindows()#cierra todas las ventanas 

if __name__ =="__main__":
    ver_camara()