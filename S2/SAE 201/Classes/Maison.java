import java.util.ArrayList;

import ardoise.*;

public class Maison extends Forme{

    private Quadrilatere murs;
    private Quadrilatere porte;
    private Chapeau toit;
    
    public Maison(String nomMa, String nomMu, String nomP, String nomT, PointPlan p1, PointPlan p2, PointPlan p3){
        super(nomMa);
        this.murs = new Quadrilatere(nomMu,p1,p2);
        this.porte= new Quadrilatere(nomP,p3,p4);
        this.toit= new Chapeau(nomT,new PointPlan(p1.getAbscisse(), p1.getOrdonnee()))
    }

    @Override
    public void deplacer(int x, int y) {
        
    }

    @Override
    public ArrayList<Segment> dessiner() {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public String getNomForme() {
        // TODO Auto-generated method stub
        return super.getNomForme();
    }

    @Override
    public void setNomForme(String arg0) {
        // TODO Auto-generated method stub
        super.setNomForme(arg0);
    }

    @Override
    public String typeForme() {
        // TODO Auto-generated method stub
        return null;
    }
}
