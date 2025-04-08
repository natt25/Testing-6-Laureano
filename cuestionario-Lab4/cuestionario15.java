public class Ejemplo {

    public static String evaluarNumero(int numero) {
        if (numero > 0) {
            return "Positivo";
        } else {
            return "Negativo";
        }
    }

    public static void main(String[] args) {
        System.out.println(evaluarNumero(5));  // Solo se ejecuta la rama donde numero > 0
    }
}
