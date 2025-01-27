import java.util.ArrayList;

import ardoise.*;

public class Quadrilatere extends Forme{

    private PointPlan p1;
    private PointPlan p2;
    private PointPlan p3;
    private PointPlan p4;

    public Quadrilatere(PointPlan p1; PointPlan p2; PointPlan p3; PointPlan p4){
        super(nom);
        this.p1 = p1;
        this.p2 = p2;
        this.p3 = p3;
        this.p4 = p4;
    }


    @Override
    public void deplacer(int x, int y) {
        this.p1.deplacer(x, y);
        this.p2.deplacer(x, y);
        this.p3.deplacer(x, y);
        this.p4.deplacer(x, y);  
    }

    @Override
    public ArrayList<Segment> dessiner() {
        return null;
    }

    @Override
    public String getNomForme() {
        
        return super.getNomForme();
    }

    @Override
    public void setNomForme(String n) {
        super.setNomForme(n);
    }

    @Override
    public String toString() {
        return "";
    }

    @Override
    public String typeForme() {
        return null;
    }}
