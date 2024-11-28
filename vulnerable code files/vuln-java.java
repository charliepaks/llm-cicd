import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class VulnerableServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws   
 ServletException, IOException   
 {
        String userInput = request.getParameter("user_input");
        response.getWriter().println("Hello, " + userInput + "!");
    }
}