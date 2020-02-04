package tiw.tiw6.storm.data;

/**
 * Une tortue est représentée en JSON comme suit:
 *     {"id":0,"top":523,"position":4,"nbDevant":8,"nbDerriere":1,"total":10}
 */
public class Tortoise {

    private int id = 0;
    private long top = 0L;
    private int position = 0;
    private int nbDevant = 0;
    private int nbDerriere = 0;
    private int total = 0;

    // Pour l'API Jackson, utilisée pour sérialiser depuis/vers du JSON
    // Évite de forcer la présence d'attributs
    public Tortoise() {
    }

    public Tortoise(int id, long top, int position, int nbDevant, int nbDerriere, int total) {
        this.id = id;
        this.top = top;
        this.position = position;
        this.nbDevant = nbDevant;
        this.nbDerriere = nbDerriere;
        this.total = total;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public long getTop() {
        return top;
    }

    public void setTop(long top) {
        this.top = top;
    }

    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public int getNbDevant() {
        return nbDevant;
    }

    public void setNbDevant(int nbDevant) {
        this.nbDevant = nbDevant;
    }

    public int getNbDerriere() {
        return nbDerriere;
    }

    public void setNbDerriere(int nbDerriere) {
        this.nbDerriere = nbDerriere;
    }

    public int getTotal() {
        return total;
    }

    public void setTotal(int total) {
        this.total = total;
    }
}
