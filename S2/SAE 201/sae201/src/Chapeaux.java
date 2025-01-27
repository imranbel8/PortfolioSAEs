import java.util.ArrayList;
import ardoise.Forme;
import ardoise.PointPlan;
import ardoise.Segment;

public class Chapeaux extends Forme{
    private PointPlan p1;
    private PointPlan p2;
    private PointPlan p3;

    public Chapeaux() {
        super();
    }

    public Chapeaux(PointPlan p1, PointPlan p2, PointPlan p3) throws ColineaireException {
        if (MethodeTest.sontColineaires(p1, p2, p3)) {
            throw new ColineaireException("Les points sont colinéaires, impossible de construire un chapeau !");
        }
        this.p1 = p1;
        this.p2 = p2;
        this.p3 = p3;
        this.setNomForme("Chapeaux");
    }

    public PointPlan getPoint1() {
        return this.p1;
    }

    public PointPlan getPoint2() {
        return this.p2;
    }

    public PointPlan getPoint3() {
        return this.p3;
    }

    public void setPoint1(PointPlan p) {
        this.p1 = p;
    }

    public void setPoint2(PointPlan p) {
        this.p2 = p;
    }

    public void setPoint3(PointPlan p) {
        this.p3 = p;
    }

    @Override
    public void deplacer(int x, int y) {
        int depx1 = this.p1.getAbscisse() + x;
        int depy1 = this.p1.getOrdonnee() + y;
        this.p1.setAbscisse(depx1);
        this.p1.setOrdonnee(depy1);

        int depx2 = this.p2.getAbscisse() + x;
        int depy2 = this.p2.getOrdonnee() + y;
        this.p2.setAbscisse(depx2);
        this.p2.setOrdonnee(depy2);

        int depx3 = this.p3.getAbscisse() + x;
        int depy3 = this.p3.getOrdonnee() + y;
        this.p3.setAbscisse(depx3);
        this.p3.setOrdonnee(depy3);

        this.dessiner();
    }

    @Override
    public ArrayList<Segment> dessiner() {
        ArrayList<Segment> segments = new ArrayList<Segment>();
        Segment s1 = new Segment(p1, p2);
        Segment s2 = new Segment(p2, p3);
        segments.add(s1);
        segments.add(s2);
        return segments;
    }

    @Override
    public String typeForme() {
        return "C";
    }

    public String toString() {
        return "[Point1" + this.getPoint1() + ", Point2" + this.getPoint2() + ", Point3" + this.getPoint3() + "]";
    }  
}
