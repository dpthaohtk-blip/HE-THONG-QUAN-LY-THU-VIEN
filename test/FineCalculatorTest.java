import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class FineCalculatorTest {

    // Test Case 1: Không bị phạt (quá hạn <= 0 ngày)
    @Test
    public void testNoFine() {
        // 1. Arrange (Chuẩn bị)
        FineCalculator calc = new FineCalculator();
        int days = 0;
        double expected = 0;
        
        // 2. Act (Thực thi)
        double actual = calc.calculate(days);
        
        // 3. Assert (Kiểm tra kết quả)
        assertEquals(expected, actual, 0.01);
    }

    // Test Case 2: Phạt bình thường (quá hạn <= 10 ngày)
    @Test
    public void testNormalFine() {
        // 1. Arrange
        FineCalculator calc = new FineCalculator();
        int days = 5;
        double expected = 25000; // 5 * 5000 = 25000
        
        // 2. Act
        double actual = calc.calculate(days);
        
        // 3. Assert
        assertEquals(expected, actual, 0.01);
    }

    // Test Case 3: Phạt nặng (quá hạn > 10 ngày, cộng thêm 20%)
    @Test
    public void testHeavyFine() {
        // 1. Arrange
        FineCalculator calc = new FineCalculator();
        int days = 11;
        double expected = 66000; // (11 * 5000) * 1.2 = 66000
        
        // 2. Act
        double actual = calc.calculate(days);
        
        // 3. Assert
        assertEquals(expected, actual, 0.01);
    }
}