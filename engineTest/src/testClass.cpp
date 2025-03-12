#include <gtest/gtest.h>
#include "testFile.hpp"

TEST(testClass, get) 
{
    TestClass cl{};
    EXPECT_EQ(cl.get(), 42);
}
