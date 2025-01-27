import ardoise.PointPlan;

public class MethodeTest {
    public static boolean sontColineaires(PointPlan p1, PointPlan p2) {
        if ( p1.getAbscisse() == p2.getAbscisse()) {
            return true;
        }
        else if ( p1.getOrdonnee() == p2.getOrdonnee()) {
            return true;
        }
        else { return false; }
    }

    public static boolean sontColineaires(PointPlan p1, PointPlan p2, PointPlan p3) {
        if ( MethodeTest.sontColineaires(p1, p2) && MethodeTest.sontColineaires(p1, p3) && MethodeTest.sontColineaires(p2, p3)) {
            return true;
        }
        else { return false; }
    }
}
