import java.util.ArrayList;

import ardoise.*;

public class Chapeau extends Forme{

    private PointPlan p1;
    private PointPlan p2;
    private PointPlan p3;

    public Chapeau(String nom, PointPlan p1, PointPlan p2, PointPlan p3){
        super(nom);
        this.p1 = p1;
        this.p2 = p2;
        this.p3 = p3;
    }

    @Override
    public void deplacer(int x, int y) {
        this.p1.deplacer(x, y);
        this.p2.deplacer(x, y);
        this.p3.deplacer(x, y);
    }

    @Override
    public String getNomForme() {
        return super.getNomForme();
    }

    @Override
    public void setNomForme(String n) {
        super.setNomForme(n);
    }

    public @Override
    public String toString() {
        return "";
    }
    @Override
    public String typeForme() {
        return null;
    }
    
}
