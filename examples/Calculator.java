/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package mi.calculadora;

/**
 *
 * @author Alberto Martin Cajal
 */
public class Calculadora {

    private double operando1;
    private double operando2;
    private char operacion;
    private double pivote;
    
    public double getOperando1 (){
        return operando1;
    }
    
    public double getOperando2 (){
        return operando2;
    }
    public char getOperacion (){
        return operacion;
    }

    public double getPivote (){
        return pivote;
    }
    public void setOperando1 (double operando){
        operando1 = operando;
    }
    
    public void setOperando2 (double operando){
        operando2 = operando;
    }
    
    public void setOperacion (char operacion){
        this.operacion = operacion;
    }

    public void setPivote (double pivote){
        this.pivote = pivote;
    }
    public double opera () {
        switch (operacion){
            case '+': return (operando1 + operando2); 
            case '-': return (operando1 - operando2); 
            case '*': return (operando1 * operando2); 
            case '/': return (operando1 / operando2); 
            default: return 0;
        }
        
    }

}
            

