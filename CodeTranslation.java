import java.io.*;
import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

public class CodeTranslation {

    public static void main(String[] args) {
        // =========================
        // Step 1: Generate test data CSV
        // =========================
        String[] majors = {"Math", "Biology"};
        try (PrintWriter writer = new PrintWriter(new File("students_test.csv"))) {
            writer.println("Name,GPA,Major");
            for (int i = 1; i <= 20; i++) {
                String name = "Student" + i;
                double gpa = ThreadLocalRandom.current().nextDouble(1.0, 4.0);
                gpa = Math.round(gpa * 100.0) / 100.0; // round to 2 decimals
                String major = majors[new Random().nextInt(majors.length)];
                writer.println(name + "," + gpa + "," + major);
            }
            System.out.println("Test data CSV 'students_test.csv' created.");
        } catch (FileNotFoundException e) {
            System.out.println("Error creating CSV file: " + e.getMessage());
        }

        // =========================
        // Step 2: Read CSV into map
        // =========================
        Map<String, double[]> students = new LinkedHashMap<>();
        try (BufferedReader br = new BufferedReader(new FileReader("students_test.csv"))) {
            String line = br.readLine(); // skip header
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",");
                String name = parts[0];
                double gpa = Double.parseDouble(parts[1]);
                double major = parts[2].trim().equals("Math") ? 1.0 : 2.0; // 1=Math, 2=Biology
                students.put(name, new double[]{gpa, major});
            }
        } catch (IOException e) {
            System.out.println("Error reading CSV: " + e.getMessage());
        }

        // =========================
        // Step 3: Compute average GPA
        // =========================
        double totalGpa = 0.0;
        for (double[] info : students.values()) {
            totalGpa += info[0];
        }
        double averageGpa = totalGpa / students.size();
        System.out.printf("\nAverage GPA: %.2f\n", averageGpa);

        // =========================
        // Step 4: Print above-average students
        // =========================
        System.out.println("Above-average students:");
        for (Map.Entry<String, double[]> entry : students.entrySet()) {
            if (entry.getValue()[0] > averageGpa) {
                System.out.printf("%s: %.2f\n", entry.getKey(), entry.getValue()[0]);
            }
        }

        // =========================
        // Step 5: Predict scholarships
        // =========================
        System.out.println("Students predicted to earn scholarships:");
        for (Map.Entry<String, double[]> entry : students.entrySet()) {
            double gpa = entry.getValue()[0];
            double major = entry.getValue()[1];
            if (major == 1.0 && gpa >= 3.5) { // Math students
                System.out.printf("%s: %.2f\n", entry.getKey(), gpa);
            } else if (major == 2.0 && gpa >= 2.75) { // Biology students
                System.out.printf("%s: %.2f\n", entry.getKey(), gpa);
            }
        }
    }
}