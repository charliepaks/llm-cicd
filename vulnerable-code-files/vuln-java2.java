import java.sql.*;

public class VulnerableSQL {
    public static void main(String[] args) {
        String username = "your_username";
        String password = "your_password";
        String databaseUrl = "jdbc:mysql://localhost:3306/mydatabase";

        try (Connection conn = DriverManager.getConnection(databaseUrl, username, password)) {
            String userInput = "'; DROP TABLE users; --"; // Malicious input
            String query = "SELECT * FROM users WHERE username = '" + userInput + "'";
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);
            // ... process the result set
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}